from rest_framework import serializers
from .models import MingSubway

class MingSubwaySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()

    class Meta:
        model = MingSubway
        fields = ['name', 'description']
