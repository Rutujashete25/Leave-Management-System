from django.urls import path
from .views import RegistrationView,customlogin, home 
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('sign-up/<int:pk>/', RegistrationView.as_view(), name="sign-up"),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('login/', customlogin.as_view(), name='login'),
    path('',home, name="home"),
]