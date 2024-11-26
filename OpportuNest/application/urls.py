from django.urls import path, include

from OpportuNest.application import views

urlpatterns = [
    path('<int:job_id>/', include([
        path('create-application/', views.CreateApplicationView.as_view(), name='create-application'),
    ])),
    path('<int:pk>/', include([
        path('details-application/', views.DetailApplicationView.as_view(), name='details-application'),
        path('accept-application/', views.accept_application, name='accept-application'),
        path('reject-application/', views.reject_application, name='reject-application'),
        path('download-resume/', views.view_resume, name='view-resume'),
    ]))
]