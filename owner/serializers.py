from rest_framework import serializers
from .models import Owner


class OwnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Owner
        fields = ('name', 'age', 'national_code', 'total_toll_paid')

