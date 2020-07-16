from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='weather_home'),
    path('update_pref/', views.update_pref, name='pref'),
    path('about/', views.about, name='about')
]