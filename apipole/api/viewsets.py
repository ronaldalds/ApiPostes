from apipole import models
from apipole.api import serializers
from rest_framework import viewsets


class PoleViewSet(viewsets.ModelViewSet):
    queryset = models.Pole.objects.all()
    serializer_class = serializers.PoleSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        search = self.request.query_params.get('aprovado', None)
        if search is not None:
            qs = qs.filter(approval=search)
        return qs
