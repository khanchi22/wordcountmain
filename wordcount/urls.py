
from django.urls import path
from . import views


urlpatterns = [
     path('', views.homepage, name='home'),
     path('count/', views.counting, name='count'),
     path('about/', views.about, name='about us'),
]
