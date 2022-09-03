from apipole import models
from rest_framework import serializers


class PoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pole
        fields = '__all__'
