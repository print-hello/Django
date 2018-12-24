from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def show_views(request):

    return render(request, 'menu.html', locals())
