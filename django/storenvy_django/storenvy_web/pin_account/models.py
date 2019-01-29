from __future__ import unicode_literals
from django.db import models


class Account(models.Model):
    email = models.CharField(max_length=100, blank=True, null=True)
    pw = models.CharField(max_length=50, blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    home_page = models.CharField(max_length=100, blank=True, null=True)
    upload_web = models.CharField(max_length=255)
    upload_computer = models.CharField(max_length=255)
    upload_done = models.IntegerField()
    upload_time = models.DateField(blank=True, null=True)
    created_boards = models.IntegerField()
    content = models.TextField(blank=True, null=True)
    login_times = models.IntegerField()
    add_time = models.DateTimeField()
    action_time = models.DateField()
    action_computer = models.CharField(max_length=50)
    register_computer = models.CharField(max_length=255)
    port = models.IntegerField()
    ip = models.CharField(max_length=255, blank=True, null=True)
    setting_other = models.IntegerField()
    cookie = models.CharField(max_length=10000, blank=True, null=True)
    agent = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account'


class Configuration(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    random_browsing_control = models.IntegerField()
    browsing_pic_min_num = models.IntegerField()
    browsing_pic_max_num = models.IntegerField()
    access_home_page_control = models.IntegerField()
    save_pic_control = models.IntegerField()
    upload_pic_control = models.IntegerField()
    upload_pic_min_num = models.IntegerField()
    upload_pic_max_num = models.IntegerField()
    follow_num = models.IntegerField()
    pin_self_count = models.IntegerField()
    scroll_num = models.IntegerField()
    create_board_num = models.IntegerField()
    search_words_count = models.IntegerField()
    save_pic_from_homepage_control = models.IntegerField()
    click_specific_pin_control = models.IntegerField()
    priority = models.IntegerField()
    content = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'configuration'
