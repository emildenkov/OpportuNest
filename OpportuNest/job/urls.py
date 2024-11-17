from django.urls import path

from OpportuNest.job import views

urlpatterns = [
    path('job-list/', views.JobListView.as_view(), name='job-list'),
    path('add-job/', views.AddJobView.as_view(), name='add-job'),

]