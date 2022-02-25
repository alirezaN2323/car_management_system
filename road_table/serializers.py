from rest_framework.serializers import ModelSerializer
from .models import AllNode


class AllNodeSerializer(ModelSerializer):
    class Meta:
        model = AllNode
        fields = ('car', 'date', 'location')

