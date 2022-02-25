# from django.db import models
from django.contrib.gis.db import models


class TollStation(models.Model):
    name = models.CharField(verbose_name='Name', max_length=55)
    toll_per_cross = models.PositiveIntegerField(verbose_name='toll_per_cross')
    location = models.PointField(verbose_name='location')

    class Meta:
        verbose_name = 'Toll Station'
        verbose_name_plural = 'Toll Stations'
        db_table = 'toll_station'

    def __str__(self):
        return f"{self.name}"
