from django.db import models
from django.contrib.gis.db import models
from vehicle.models import Vehicle


class AllNode(models.Model):
    car = models.ForeignKey(Vehicle, on_delete=models.CASCADE,
                            related_name='all_nodes')
    date = models.DateTimeField(verbose_name='date')
    location = models.PointField(verbose_name='location')

    class Meta:
        verbose_name = 'AllNode'
        verbose_name_plural = 'AllNodes'
        db_table = 'all_nodes'

