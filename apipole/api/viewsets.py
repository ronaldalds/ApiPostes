from apipole import models
from apipole.api import serializers
from rest_framework import viewsets


class PoleViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PoleSerializer
    queryset = models.Pole.objects.all()
