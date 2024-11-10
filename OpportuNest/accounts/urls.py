from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path

from OpportuNest.accounts import views

urlpatterns = [
    path('select-account-type/', views.AccountSelectView.as_view(), name='account_select_type'),
    path('register-company/', views.CompanyRegistrationView.as_view(), name='register_company'),
    path('register-seeker/', views.SeekerRegistrationView.as_view(), name='register_seeker'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]