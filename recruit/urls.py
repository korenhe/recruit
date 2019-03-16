"""recruit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

from interviews import views as interviewsViews
from jobs import views as jobsViews
from candidates import views as candidatesViews
from recruiters import views as recruitersViews
from dashboards import views as dashboardViews
from django.contrib.auth.models import User
from django.views.static import serve

urlpatterns = [
    url(r'^$', dashboardViews.dashboards, name='dashboards'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^jobs/$', jobsViews.view_jobs, name='jobs'),
    url(r'^jobs/(?P<job_id>\d+)/$', jobsViews.view_job_details, name='job_details'),
    url(r'^candidates/apply/$', candidatesViews.apply, name='candidate_apply'),
    url(r'^candidates/apply/success/$', candidatesViews.apply_success, name='candidate_apply_success'),
    url(r'^recruiters/', recruitersViews.view_recruiters, name='recruiters'),
    url(r'^available/(?P<bu_id>\d+)/$', interviewsViews.available, name='available'),
    url(r'^availability/(?P<bu_id>\d+)/$', interviewsViews.availability, name='availability'),
    url(r'^interviews/', interviewsViews.interview_requests, name='interviews'),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, 'show_indexes': settings.DEBUG}),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
