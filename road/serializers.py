from rest_framework.serializers import ModelSerializer
from .models import Road


class RoadSerializer(ModelSerializer):
    class Meta:
        model = Road
        fields = ('name', 'width', 'geom')