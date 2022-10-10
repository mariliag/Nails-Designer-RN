from ast import increment_lineno
from django.http import HttpResponse
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import HomeView, LoginView

urlpatterns = [
    path("", HomeView.as_view(), name='home'),
    path('login/', auth_views.LoginView.as_view(
        template_name='login.html'
    ), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]