from django.shortcuts import render
from .models import *
import datetime


def pin_views(request):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d")
    s = Account.objects.using('pin_db').filter(port__gte=100)
    all_count = Account.objects.using('pin_db').filter(port__gte=100).count()
    right_count = Account.objects.using('pin_db').filter(state=1).filter(port__gte=100).count()
    ip_count = Account.objects.using('pin_db').filter(state=2).filter(port__gte=100).count()
    run_today = Account.objects.using('pin_db').filter(action_time__gte=current_time).count()
    config = Configuration.objects.using('pin_db')
    return render(request, 'pin.html', locals())