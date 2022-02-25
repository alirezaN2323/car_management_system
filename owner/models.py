from django.contrib.gis.geos import Point
from django.db import models
from django.contrib.gis.db import models


class Owner(models.Model):
    name = models.CharField(verbose_name='Name', max_length=55)
    age = models.PositiveSmallIntegerField(verbose_name='Age')
    national_code = models.CharField(max_length=10,
                                     verbose_name='National Code')
    total_toll_paid = models.PositiveIntegerField(
        verbose_name='Total Toll Paid')

    class Meta:
        verbose_name = 'Owner'
        verbose_name_plural = 'Owners'
        db_table = 'owner'

