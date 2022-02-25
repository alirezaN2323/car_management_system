# from django.db import models
from django.contrib.gis.db import models
from owner.models import Owner


class Vehicle(models.Model):
    TYPE_CHOICES = (
        ('S', 'Small'),
        ('B', 'Big')
    )
    input_id = models.PositiveIntegerField(verbose_name='Input ID')
    color = models.CharField(verbose_name='Color', max_length=55)
    length = models.FloatField(verbose_name='Length')
    type = models.CharField(verbose_name='type', choices=TYPE_CHOICES,
                            max_length=1)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE,
                              related_name='vehicles')
    load_valume = models.FloatField(verbose_name='Load Valume', blank=True,
                                    null=True)

    class Meta:
        verbose_name = 'Vehicle'
        verbose_name_plural = 'Vehicles'
        db_table = 'vehicle'

    def __str__(self):
        return f"{self.color} {self.type} vehicle for {self.owner.name}"


# class GeneralVehicle(Vehicle):
#     owner = models.ForeignKey(to=Owner, on_delete=models.CASCADE,
#                               related_name='general_vehicles')
#
#     class Meta:
#         verbose_name = 'General Vehicle'
#         verbose_name_plural = 'General Vehicles'
#         db_table = 'general_vehicle'
#
#
# class HeavyVehicle(Vehicle):
#     owner = models.OneToOneField(Owner, unique=True, on_delete=models.CASCADE)
#     load_valume = models.FloatField(verbose_name='Load Valume', blank=True,
#                                     null=True)
#
#     class Meta:
#         verbose_name = 'Heavy Vehicle'
#         verbose_name_plural = 'Heavy Vehicles'
#         db_table = 'heavy_vehicle'
