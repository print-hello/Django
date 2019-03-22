from django.urls import path
from . import views


app_name = 'pinBabyAccount'
urlpatterns = [
    path('', views.index, name='index'),
]
