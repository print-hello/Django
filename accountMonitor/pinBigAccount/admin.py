from django.contrib import admin
from .models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'state', 'belong']
    list_filter = ['belong']
    search_fields = ['email']
    fieldsets = [
        (None, {'fields': ['email']}),
        (None, {'fields': ['pw']}),
        (None, {'fields': ['domain']}),
        (None, {'fields': ['vpn']}),
        ('状态：1：正常----9：密码需要修改', {'fields': ['state']}),
    ]

admin.site.register(Account, AccountAdmin)
admin.site.site_header = '账号管理'
admin.site.site_title = '后台'