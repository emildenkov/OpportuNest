from django.urls import path

from OpportuNest.review import views

urlpatterns = [
    path('create-review/', views.CreateReviewView.as_view(), name='create-review'),
]