from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome),
    path('profile/', views.profile_page),
    path('settings/', views.settings)
    
]