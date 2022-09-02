from uuid import uuid4

from django.db import models


class Pole(models.Model):
    id_pole = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    owner = models.CharField(max_length=50)
    type_pole = models.CharField(max_length=50)
    height = models.IntegerField()
    traction = models.CharField(max_length=50)
    rede = models.CharField(max_length=50)
    house = models.IntegerField()
    commerce = models.CharField(max_length=50)
    building = models.CharField(max_length=50)
    equipment = models.CharField(max_length=50)
    code_csi = models.CharField(max_length=50)
    occupants = models.CharField(max_length=50)
    image = models.CharField(max_length=50)
    date_creation = models.DateField(auto_now_add=True)
    date_upgrade = models.DateField()
    approval = models.CharField(max_length=50)
    date_approval = models.DateField()
    protocol_approval = models.CharField(max_length=50)
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
