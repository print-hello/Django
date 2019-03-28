from django.db import models


class BusinessAccountDomain(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    email = models.CharField(max_length=255, blank=True, null=True)
    home_page = models.CharField(max_length=255, blank=True, null=True)
    domain = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'business_account_domain'


class BusinessPinViews(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    user = models.CharField(max_length=255, blank=True, null=True)
    page_view_num = models.IntegerField(blank=True, null=True)
    spider_time = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'business_pin_views'


class BusinessSpiderInfo(models.Model):
    user = models.CharField(max_length=50)
    created_at = models.DateTimeField(blank=True, null=True)
    repin_count = models.IntegerField()
    imgsaves = models.IntegerField()
    url = models.CharField(primary_key=True, max_length=200)
    link = models.CharField(max_length=2000, blank=True, null=True)
    domain = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'business_spider_info'
