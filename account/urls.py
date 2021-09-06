from django.urls import path

from . import views

urlpatterns = [
    path('', views.RegisterAPI.as_view(), name='register'),
]