from django.db import models


class Storenvy(models.Model):
	store_id =models.IntegerField()
	store_name = models.CharField(max_length=255)
	sale_today = models.IntegerField(default = '0')
	sale_all = models.IntegerField()
	url = models.CharField(max_length=255)
	spider_time = models.DateField(blank=True, null=True)

	class Meta:
		db_table = 'Storenvy'