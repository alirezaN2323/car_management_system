from rest_framework.serializers import ModelSerializer
from vehicle.models import Vehicle


class VehicleSerializer(ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('color', 'length', 'type', 'owner', 'load_valume')


