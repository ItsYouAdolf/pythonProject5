from django.urls import path
from . import views

urlpatterns = [
    path('', views.istoriea, name='istoriea'),
]