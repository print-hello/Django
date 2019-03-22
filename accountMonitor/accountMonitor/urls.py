from django.contrib import admin
from django.urls import path, include
from menu.views import show_views


urlpatterns = [
    path('menu/', show_views),
    path('menu/pinBigAccount/', include('pinBigAccount.urls')),
    path('menu/pinSmallAccount/', include('pinSmallAccount.urls')),
    path('menu/pinBabyAccount/', include('pinBabyAccount.urls')),
    path('menu/storenvy/', include('storenvy.urls')),
    path('admin/', admin.site.urls),
]
