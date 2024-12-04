from django.urls import path, include

from OpportuNest.job import views
from OpportuNest.job.views import JobListAPIView

urlpatterns = [
    path('job-list/', views.JobListView.as_view(), name='job-list'),
    path('add-job/', views.AddJobView.as_view(), name='add-job'),
    path('<int:pk>/', include([
        path('details/', views.DetailJobView.as_view(), name='job-details'),
        path('edit/', views.EditJobView.as_view(), name='edit-job'),
        path('delete/', views.DeleteJobView.as_view(), name='delete-job'),
    ])),
    path('api/jobs/', JobListAPIView.as_view(), name='api-jobs'),
]