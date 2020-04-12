from rest_framework import serializers
from .models import *


class ConsolidatedDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsolidatedData
        fields = '__all__'
