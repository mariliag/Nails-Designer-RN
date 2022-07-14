from django.urls import path
from .views import HomeView, AboutView

urlpatterns = [
    path('home', HomeView.as_view()),
    path('about', AboutView.as_view()),
    # e as outras...
]