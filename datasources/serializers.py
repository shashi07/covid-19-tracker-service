from rest_framework import serializers
from .models import *


class ConsolidatedDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsolidatedData
        fields = '__all__'

class ComparisionDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComparisionData
        fields = '__all__'


class StateWiseComparisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StateWiseData
        fields = '__all__'


class AgeWiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgeWiseData
        fields = '__all__'