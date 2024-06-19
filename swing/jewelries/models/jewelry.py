from django.db.models import PROTECT
from django.db.models import CharField
from django.db.models import ForeignKey
from django.db.models import ManyToManyField
from django.db.models import Model
from django.db.models import PositiveIntegerField
from jewelries.models.bead import Bead
from jewelries.models.hardware import Hardware

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
    strings = ManyToManyField(JewelryString, through="LinkJewelryString")

    def __str__(self):
        return self.name


class LinkJewelryBead(Model):
    """
    Jewelry bead many to many model.
    """

    jewelry = ForeignKey(Jewelry, on_delete=PROTECT)
    bead = ForeignKey(Bead, on_delete=PROTECT)
    quantity = PositiveIntegerField()

    def __str__(self):
        return f"{self.jewelry.name} - {self.bead.name} * {self.quantity}"


class LinkJewelryHardware(Model):
    """
    Jewelry hardware many to many model.
    """

    jewelry = ForeignKey(Jewelry, on_delete=PROTECT)
    hardware = ForeignKey(Hardware, on_delete=PROTECT)
    quantity = PositiveIntegerField()

    def __str__(self):
        return f"{self.jewelry.name} - {self.hardware.name} * {self.quantity}"


class LinkJewelryJewelryString(Model):
    """
    Jewelry string many to many model.
    """

    jewelry = ForeignKey(Jewelry, on_delete=PROTECT)
    string = ForeignKey(JewelryString, on_delete=PROTECT)
    quantity = PositiveIntegerField()

    def __str__(self):
        return f"{self.jewelry.name} - {self.string.name} * {self.quantity}mm"
