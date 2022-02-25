from django.contrib import admin
from .models import TollStation


@admin.register(TollStation)
class TollStationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location', 'toll_per_cross')
    list_display_links = ('id', 'name', 'location', 'toll_per_cross')

    search_fields = ('id', 'name')

