from django.db import models


class PriceTable(models.Model):
    class Meta:
        db_table = 'price_table'

    start_area = models.CharField(max_length=50)
    end_area = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
