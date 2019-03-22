from django.urls import path
from . import views


app_name = 'pinSmallAccount'
urlpatterns = [
    path('', views.index, name='index'),
]
