from django.contrib import admin
from .models import Road


@admin.register(Road)
class RoadAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'width', 'geom')
    list_display_links = ('id', 'name', 'width', 'geom')
    search_fields = ('name',)
