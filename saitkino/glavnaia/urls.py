from django.urls import path
from . import views

urlpatterns = [
    path('', views.glavnaia, name='glavnaia'),
]