# from django.db import models
from django.contrib.gis.db import models


class Road(models.Model):
    name = models.CharField(max_length=65, blank=True, null=True)
    width = models.FloatField(verbose_name='Width')
    geom = models.MultiLineStringField(verbose_name='Geometry')

    class Meta:
        verbose_name = 'Road'
        verbose_name_plural = 'Roads'
        db_table = 'road'

    def __str__(self):
        return f"road : {self.name}"



