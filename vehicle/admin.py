from django.contrib import admin
from vehicle.models import Vehicle


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('id', 'color', 'length', 'get_owner', 'type',
                    'load_valume')
    list_display_links = ('id', 'color', 'length', 'get_owner',
                          'load_valume', 'type')

    search_fields = ('color', 'id')

    def get_owner(self, obj):
        return obj.owner.name
    get_owner.short_description = "Owner"

