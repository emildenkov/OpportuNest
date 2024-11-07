from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('OpportuNest.common.urls')),
    path('accounts/', include('OpportuNest.accounts.urls')),
    path('application/', include('OpportuNest.application.urls')),
    path('company_profile/', include('OpportuNest.company_profile.urls')),
    path('job/', include('OpportuNest.job.urls')),
    path('job_seeker/', include('OpportuNest.job_seeker_profile.urls')),
    path('review', include('OpportuNest.review.urls')),
    path('skill/', include('OpportuNest.skill.urls')),
]
