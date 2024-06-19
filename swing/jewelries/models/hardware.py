from django.db.models import PROTECT
from django.db.models import CharField
from django.db.models import DecimalField
from django.db.models import ForeignKey
from django.db.models import Model
from django.db.models import URLField

from swing.jewelries.models.bead import BeadMaterial


class HardwareType(Model):
    """
    Hardware type model.
    """

    name = CharField(max_length=255)

    def __str__(self):
        return self.name


class HardwareMaterial(Model):
    """
    Hardware material model.
    """

    name = CharField(max_length=255)

    def __str__(self):
        return self.name


class Hardware(Model):
    """
    Hardware model.
    """

    name = CharField(max_length=255)
    size = DecimalField(max_digits=10, decimal_places=2)
    type = ForeignKey(HardwareType, on_delete=PROTECT)
    price = DecimalField(max_digits=10, decimal_places=2)
    link = URLField(blank=True, max_length=255)
    material = ForeignKey(BeadMaterial, on_delete=PROTECT)

    def __str__(self):
        return self.name
