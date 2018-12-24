from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import subprocess


def pin_views(request):
    s = Account.objects.using('pin_db').filter(port__gte=100)
    all_count = Account.objects.using('pin_db').filter(port__gte=100).count()
    right_count = Account.objects.using('pin_db').filter(state=1).filter(port__gte=100).count()

    return render(request, 'pin.html', locals())