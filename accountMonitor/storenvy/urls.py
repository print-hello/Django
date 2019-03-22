from django.urls import path
from . import views


urlpatterns = [
    path('', views.storenvy_order, name='storenvy_order'),
    path('crawl', views.crawl, name='crawl'),
]
