from django.db import models


class Account(models.Model):
    email = models.CharField(max_length=100, blank=True, null=True)
    pw = models.CharField(max_length=50, blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    account_group = models.IntegerField()
    home_page = models.CharField(max_length=100, blank=True, null=True)
    created_boards = models.IntegerField()
    content = models.TextField(blank=True, null=True)
    get_link_state = models.IntegerField()
    get_fans_state = models.IntegerField()
    login_times = models.IntegerField()
    add_time = models.DateTimeField()
    action_time = models.DateField()
    serach_end_time = models.DateField(blank=True, null=True)
    action_computer = models.CharField(max_length=50)
    vpn = models.CharField(max_length=50)
    vpn_class = models.CharField(max_length=50, blank=True, null=True)
    class_flag = models.IntegerField()
    readmail = models.DateField()
    serach_history = models.CharField(max_length=500)
    serach_history_other = models.CharField(max_length=500, blank=True, null=True)
    pwd_old = models.CharField(max_length=100)
    setting_other = models.IntegerField()
    pin_system_id = models.IntegerField()
    website = models.CharField(max_length=100)
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
