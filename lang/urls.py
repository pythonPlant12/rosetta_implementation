from django.urls import path
from . import views

app_name = 'lang'

urlspatterns = [
  path('', views.home, name="home")
]