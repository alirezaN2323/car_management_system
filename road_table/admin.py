from django.contrib import admin
from .models import AllNode


@admin.register(AllNode)
class AllNodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'car', 'date', 'location')
    list_display_links = ('id', 'car', 'date', 'location')
