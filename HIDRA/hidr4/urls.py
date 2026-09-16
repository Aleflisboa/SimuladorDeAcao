from django.urls import path
from . import views

urlpatterns = [
    path('ver_hidra/', views.ver_hidra, name="ver_hidra")
]