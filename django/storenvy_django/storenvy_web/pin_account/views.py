from django.shortcuts import render
from .models import *


def pin_views(request):
    s = Account.objects.using('pin_db').filter(port__gte=100)
    all_count = Account.objects.using('pin_db').filter(port__gte=100).count()
    right_count = Account.objects.using('pin_db').filter(state=1).filter(port__gte=100).count()
    ip_count = Account.objects.using('pin_db').filter(state=2).filter(port__gte=100).count()

    return render(request, 'pin.html', locals())