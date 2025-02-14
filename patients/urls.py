from django.urls import path
from . import views

urlpatterns = [
    path('', views.patients, name='patients'),
]
