from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path, include

from OpportuNest.accounts import views

urlpatterns = [
    path('select-account-type/', views.AccountSelectView.as_view(), name='account-select-type'),
    path('register-company/', views.CompanyRegistrationView.as_view(), name='register-company'),
    path('register-seeker/', views.SeekerRegistrationView.as_view(), name='register-seeker'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('<int:pk>/', include([
        path('details/', views.ProfileDetailView.as_view(), name='profile-details'),
        path('edit-seeker/', views.EditSeekerView.as_view(), name='edit-seeker'),
        path('edit-company/', views.EditCompanyView.as_view(), name='edit-company'),
        path('delete-company/', views.DeleteCompanyView.as_view(), name='delete-company'),
        path('delete-seeker/', views.DeleteSeekerView.as_view(), name='delete-seeker'),
    ]))
]