from django.db.models import PROTECT
from django.db.models import CharField
from django.db.models import DecimalField
from django.db.models import ForeignKey
from django.db.models import Model
from django.db.models import URLField


class BeadMaterial(Model):
    """
    Bead material model.
    """

    name = CharField(max_length=255)

    def __str__(self):
        return self.name


class Bead(Model):
    """
    Bead model.
    """

    name = CharField(max_length=255)
    length = DecimalField(max_digits=10, decimal_places=2)
    diameter = DecimalField(max_digits=10, decimal_places=2)
    pore_diameter = DecimalField(max_digits=10, decimal_places=2)
    price = DecimalField(max_digits=10, decimal_places=2)
    link = URLField(blank=True, max_length=255)
    material = ForeignKey(BeadMaterial, on_delete=PROTECT)

    def __str__(self):
        return self.name
