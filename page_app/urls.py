from django.urls import path 
from .import views

urlpatterns = [
    path('', views.index),
    path('contact', views.contact),
    path('work', views.work),
    path('about', views.about),
    path('coming_soon', views.coming_soon),
]