from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^sale/$', hello_views),
    url(r'^click$', crawl_views),
]
