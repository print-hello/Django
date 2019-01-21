# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
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


class AccountCount(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    all_count = models.IntegerField(blank=True, null=True)
    real_time_num = models.IntegerField(blank=True, null=True)
    last_update_time = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_count'


class BoardTemplate(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    board_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'board_template'


class Configuration(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    random_browsing_control = models.IntegerField()
    browsing_pic_min_num = models.IntegerField()
    browsing_pic_max_num = models.IntegerField()
    access_home_page_control = models.IntegerField()
    save_pic_control = models.IntegerField()
    follow_num = models.IntegerField()
    pin_self_count = models.IntegerField()
    scroll_num = models.IntegerField()
    create_board_num = models.IntegerField()
    search_words_count = models.IntegerField()
    priority = models.IntegerField()
    content = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'configuration'


class FollowUrl(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    web_url = models.CharField(max_length=255, blank=True, null=True)
    home_url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'follow_url'


class Ips(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    ip = models.CharField(max_length=20, blank=True, null=True)
    a_segment = models.IntegerField(blank=True, null=True)
    b_segment = models.IntegerField(blank=True, null=True)
    c_segment = models.IntegerField(blank=True, null=True)
    used = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ips'


class OtherPinHistory(models.Model):
    account_id = models.IntegerField()
    pin_url = models.CharField(max_length=200)
    pin_pic_url = models.CharField(max_length=255, blank=True, null=True)
    add_time = models.DateTimeField()
    hostname = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'other_pin_history'


class PinHistory(models.Model):
    account_id = models.IntegerField()
    pin_url = models.CharField(max_length=200)
    pin_pic_url = models.CharField(max_length=255, blank=True, null=True)
    add_time = models.DateTimeField()
    hostname = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pin_history'


class PortInfo(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    port = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    zone = models.CharField(max_length=255, blank=True, null=True)
    state = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'port_info'


class SearchWords(models.Model):
    word = models.CharField(max_length=100)
    state = models.IntegerField()
    boards = models.CharField(max_length=100)
    us = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'search_words'


class UserAgent(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    user_agent = models.CharField(max_length=255, blank=True, null=True)
    system = models.CharField(max_length=255, blank=True, null=True)
    terminal = models.CharField(max_length=255, blank=True, null=True)
    read_time = models.IntegerField(blank=True, null=True)
    state = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_agent'
