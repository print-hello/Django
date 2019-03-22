from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import multiprocessing
from .get_order import start_crawl

def storenvy_order(request):
    s = Storenvy.objects.using('storenvy').order_by('-sale_today')
    s_time = Storenvy.objects.using('storenvy').get(id=1)
    context = {
        's': s,
        's_time': s_time
    }
    return render(request, 'storenvy/order.html', context)


def crawl(request):
    p = multiprocessing.Process(target=start_crawl)
    p.start()
    p.join()
    return HttpResponse('数据更新完毕!')