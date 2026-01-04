from django.urls import path
from . import views

urlpatterns = [
    path('', views.pilot_status, name='pilot_status'),
]

