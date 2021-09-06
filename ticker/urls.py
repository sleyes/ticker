from django.urls import path

from . import views

urlpatterns = [
    path('', views.GetTicker.as_view(), name='get_ticker'),
]