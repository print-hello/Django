from django.db import models


class Account(models.Model):
    setting_other = models.IntegerField()
    email = models.CharField(max_length=100, blank=True, null=True)
    pw = models.CharField(max_length=50, blank=True, null=True)
    email_pwd = models.CharField(max_length=50, blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    priority = models.IntegerField()
    home_page = models.CharField(max_length=100, blank=True, null=True)
    domain = models.CharField(max_length=255, blank=True, null=True)
    domain_state = models.IntegerField(blank=True, null=True)
    login_times = models.IntegerField()
    add_time = models.DateTimeField()
    action_time = models.DateField()
    auto_login_time = models.DateField()
    action_computer = models.CharField(max_length=50)
    belong = models.CharField(max_length=50, blank=True, null=True)
    computer_state = models.IntegerField(blank=True, null=True)
    mac_adress = models.CharField(max_length=255, blank=True, null=True)
    vpn = models.CharField(max_length=50)
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
    auto_last_update_time = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_count'
