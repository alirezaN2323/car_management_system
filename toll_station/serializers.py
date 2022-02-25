from .models import TollStation
from rest_framework import serializers


class TollStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TollStation
        fields = ('name', 'toll_per_cross', 'location')