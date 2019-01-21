from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import subprocess


def hello_views(request):
    s = Storenvy.objects.all()
    s_time = Storenvy.objects.get(id=1)
    # time = s_time.spider_time
    return render(request, 'hello.html', locals())

def crawl_views(request):
    p = subprocess.Popen(
        'cmd.exe /c' + 'E:\\django\\storenvy_django\\storenvy_web\\order\\get_order.py', stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    p.wait()
    return HttpResponse('数据更新完毕!')







