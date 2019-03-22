from django.shortcuts import render


def show_views(request):
    base_url = 'http://172.16.254.251:8848/menu'
    storenvy_control = base_url + '/storenvy'
    pinBigAccount_control = base_url + '/pinBigAccount'
    admin_control = base_url.replace('/menu', '') + '/admin'
    context = {'storenvy_control': storenvy_control,
               'pinBigAccount_control': pinBigAccount_control,
               'admin_control': admin_control}
    return render(request, 'menu/index.html', context)


def global_params(request):
    base_url = 'http://172.16.254.251:8848/menu'
    pinBigAccount_control = base_url + '/pinBigAccount'
    pinSmallAccount_control = base_url + '/pinSmallAccount'
    pinBabyAccount_control = base_url + '/pinBabyAccount'
    crawl_button = base_url + '/storenvy/crawl'
    return {'pinBigAccount_control': pinBigAccount_control,
            'pinSmallAccount_control': pinSmallAccount_control,
            'pinBabyAccount_control': pinBabyAccount_control,
            'crawl_button': crawl_button}

