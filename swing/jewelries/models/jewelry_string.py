from django.db.models import CharField
from django.db.models import DecimalField
from django.db.models import Model
from django.db.models import URLField


class JewelryString(Model):
    """
    Jewelry string model.
    """

    name = CharField(max_length=255)
    price = DecimalField(max_digits=10, decimal_places=2)  # per mm
    link = URLField(blank=True, max_length=255)

    def __str__(self):
        return self.name
