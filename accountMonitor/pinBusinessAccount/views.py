from django.shortcuts import render
from .models import *
import datetime
from django.shortcuts import HttpResponse
# from django.db.models import Count
from .forms import ChoiceDateForm
from django.db import connections


def my_custom_sql(btime, etime):
    with connections['pin_data_crawl'].cursor() as cursor:
        cursor.execute("SELECT b.user, a.page_view_num, count(b.url) as today_count from (SELECT business_pin_views.user,business_pin_views.`spider_time`,business_pin_views.`page_view_num` FROM (SELECT max(`spider_time`) max_time,`user` FROM `business_pin_views` group by `user`) bbb left join `business_pin_views` on `business_pin_views`.`spider_time` = bbb.max_time and `business_pin_views`.user = bbb.user group by business_pin_views.user) a left join business_spider_info b on a.user=b.user where b.created_at>%s and b.created_at<%s group by b.user order by a.page_view_num desc",
                       (btime, etime))
        row = cursor.fetchall()
    return row


def index(request):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d")
    yestoday = '2019-01-01'
    # info = BusinessSpiderInfo.objects.using('pin_data_crawl').values('user').filter(
    #     created_at__gte=yestoday, created_at__lt=current_time
    # ).annotate(today_count=Count('user'))
    spider_time = BusinessPinViews.objects.using(
        'pin_data_crawl').order_by('-id')[:1]
    info = my_custom_sql(yestoday, current_time)
    btime = (datetime.datetime.now() +
             datetime.timedelta(days=-1)).strftime("%Y-%m-%d")
    etime = current_time
    context = {
        'info': info,
        'current_time': current_time,
        'yestoday': yestoday,
        'spider_time': spider_time[0],
        'btime': btime,
        'etime': etime,
    }
    return render(request, 'pinBusinessAccount/pinBusiness.html', context)


def choiceDate(request):
    form = ChoiceDateForm()
    context = {
        'form': form
    }
    return render(request, 'pinBusinessAccount/pinBusiness.html', context)


def search_form(request):
    spider_time = BusinessPinViews.objects.using(
        'pin_data_crawl').order_by('-id')[:1]
    current_time = datetime.datetime.now().strftime("%Y-%m-%d")
    if 'btime' or 'etime' in request.GET:
        btime = request.GET['btime']
        etime = request.GET['etime']
        if not etime:
            etime = current_time
        # info = BusinessSpiderInfo.objects.using('pin_data_crawl').values('user').filter(
        #     created_at__gte=btime, created_at__lt=etime).annotate(
        #     today_count=Count('user'))
        info = my_custom_sql(btime, etime)
        context = {
            'info': info,
            'btime': btime,
            'etime': etime,
            'spider_time': spider_time[0]
        }
        return render(request, 'pinBusinessAccount/pinBusiness.html', context)
    else:
        message = 'You submitted an empty form.'
        return HttpResponse(message)


def more_info(request):
    with connections['pin_data_crawl'].cursor() as cursor:
        cursor.execute(
            "SELECT spider_time from business_pin_views group by spider_time desc")
        all_time = cursor.fetchall()
        last_time = all_time[0][0]
        other_time = all_time[1][0]
        cursor.execute("DROP TABLE IF EXISTS tmp_table")
        cursor.execute(
            "CREATE temporary table tmp_table select * from business_pin_views")
        cursor.execute("select b.user, a.page_view_num, b.page_view_num from (select * from tmp_table where spider_time=%s) a right outer join business_pin_views b on a.user=b.user where b.spider_time=%s group by user order by b.page_view_num desc",
                       (other_time, last_time))
        row = cursor.fetchall()
    context = {
        'row': row,
        'last_time': last_time,
        'other_time': other_time,
    }
    return render(request, 'pinBusinessAccount/moreViews.html', context)
