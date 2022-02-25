from django.contrib import admin
from owner.models import Owner


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'national_code', 'total_toll_paid',
                    'get_own_cars')
    list_display_links = ('id', 'name', 'age', 'national_code',
                          'total_toll_paid')
    search_fields = ('id', 'name', 'national_code')

    def get_own_cars(self, obj):
        return [car_obj for car_obj in obj.vehicles.all()]
    get_own_cars.short_description = 'Own Vehicles'
