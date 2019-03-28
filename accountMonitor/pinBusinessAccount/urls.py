from django.urls import path
from . import views


app_name = 'pinBusinessAccount'
urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search_form),
    path('moreViews', views.more_info),
]