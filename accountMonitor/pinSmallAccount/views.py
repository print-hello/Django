from django.shortcuts import render
from .models import *
import datetime


def index(request):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d")
    all_account = Account.objects.using('pinterest').filter(state__lt=99).filter(state__gte=1)
    account_info = all_account.order_by('action_time')
    all_count = all_account.count()
    right_count = all_account.filter(state=1).count()
    run_today = all_account.filter(action_time__gte=current_time).count()
    context = {'account_info': account_info,
               'run_today': run_today,
               'all_count': all_count,
               'right_count': right_count}
    return render(request, 'pinSmallAccount/pinSmall.html', context)
