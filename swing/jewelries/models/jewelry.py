from django.db.models import PROTECT
from django.db.models import BooleanField
from django.db.models import CharField
from django.db.models import ForeignKey
from django.db.models import ManyToManyField
from django.db.models import Model
from django.db.models import PositiveIntegerField

from swing.jewelries.models.bead import Bead
from swing.jewelries.models.hardware import Hardware
from swing.jewelries.models.jewelry_string import JewelryString


class Series(Model):
    """
    Series model.
    """

    name = CharField(max_length=255)

    def __str__(self):
        return self.name


class JewelryType(Model):
    """
    Jewelry type model.
    """

    name = CharField(max_length=255)

    def __str__(self):
        return self.name


class Jewelry(Model):
    """
    Jewelry model.
    """

    name = CharField(max_length=255)
    serious = ForeignKey(Series, on_delete=PROTECT)
    type = ForeignKey(JewelryType, on_delete=PROTECT)
    beads = ManyToManyField(Bead, through="LinkJewelryBead")
    hardwares = ManyToManyField(Hardware, through="LinkJewelryHardware")
    strings = ManyToManyField(JewelryString, through="LinkJewelryJewelryString")

    def __str__(self):
        return self.name

    def length(self):
        length = 0
        for linkjewelrybead in self.linkjewelrybead_set.all():
            length += linkjewelrybead.bead.length * linkjewelrybead.quantity
        for linkjewelryhardware in self.linkjewelryhardware_set.filter(is_main=True):
            length += linkjewelryhardware.hardware.length * linkjewelryhardware.quantity
        return length

    def price(self):
        price = 0
        for linkjewelrybead in self.linkjewelrybead_set.all():
            price += linkjewelrybead.bead.price * linkjewelrybead.quantity
        for linkjewelryhardware in self.linkjewelryhardware_set.all():
            price += linkjewelryhardware.hardware.price * linkjewelryhardware.quantity
        for linkjewelryjewelrystring in self.linkjewelryjewelrystring_set.all():
            price += (
                linkjewelryjewelrystring.jewelry_string.price
                * linkjewelryjewelrystring.quantity
            )
        return price


class LinkJewelryBead(Model):
    """
    Jewelry bead many to many model.
    """

    jewelry = ForeignKey(Jewelry, on_delete=PROTECT)
    bead = ForeignKey(Bead, on_delete=PROTECT)
    quantity = PositiveIntegerField()

    class Meta:
        unique_together = ["jewelry", "bead"]

    def __str__(self):
        return f"{self.jewelry.name} - {self.bead.name} * {self.quantity}"


class LinkJewelryHardware(Model):
    """
    Jewelry hardware many to many model.
    """

    jewelry = ForeignKey(Jewelry, on_delete=PROTECT)
    hardware = ForeignKey(Hardware, on_delete=PROTECT)
    quantity = PositiveIntegerField()
    is_main = BooleanField(null=False)  # included in the main body or not

    class Meta:
        unique_together = ["jewelry", "hardware"]

    def __str__(self):
        return f"{self.jewelry.name} - {self.hardware.name} * {self.quantity}"


class LinkJewelryJewelryString(Model):
    """
    Jewelry string many to many model.
    """

    jewelry = ForeignKey(Jewelry, on_delete=PROTECT)
    jewelry_string = ForeignKey(JewelryString, on_delete=PROTECT)
    quantity = PositiveIntegerField()

    class Meta:
        unique_together = ["jewelry", "jewelry_string"]

    def __str__(self):
        return f"{self.jewelry.name} - {self.jewelry_string.name} * {self.quantity}mm"
