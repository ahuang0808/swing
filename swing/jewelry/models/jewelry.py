from django.db.models import PROTECT
from django.db.models import BooleanField
from django.db.models import CharField
from django.db.models import DecimalField
from django.db.models import ForeignKey
from django.db.models import ManyToManyField
from django.db.models import Model
from django.db.models import PositiveIntegerField
from django.db.models import TextField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from swing.jewelry.models.bead import Bead
from swing.jewelry.models.hardware import Hardware
from swing.jewelry.models.jewelry_string import JewelryString
from swing.package.models.package import Package


class Series(Model):
    """
    Series model.
    """

    name = CharField(max_length=255, verbose_name=_("Name"))

    class Meta:
        verbose_name = _("Series")
        verbose_name_plural = _("Series")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("admin:jewelry_series_change", args=[str(self.id)])


class JewelryType(Model):
    """
    Jewelry type model.
    """

    name = CharField(max_length=255, verbose_name=_("Name"))

    class Meta:
        verbose_name = _("Jewelry Type")
        verbose_name_plural = _("Jewelry Types")

    def __str__(self):
        return self.name


class Jewelry(Model):
    """
    Jewelry model.
    """

    name = CharField(max_length=255, verbose_name=_("Name"))
    title = CharField(max_length=255, verbose_name=_("Title"))
    serious = ForeignKey(Series, on_delete=PROTECT, verbose_name=_("Serious"))
    type = ForeignKey(JewelryType, on_delete=PROTECT, verbose_name=_("Type"))
    length = PositiveIntegerField(
        verbose_name=_("Length"),
        help_text=_("The unit is millimeter."),
    )
    price = DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Price"))
    introduction = TextField(blank=True, verbose_name=_("Introduction"))
    inspiration = TextField(blank=True, verbose_name=_("Inspiration"))
    beads = ManyToManyField(Bead, through="LinkJewelryBead")
    hardwares = ManyToManyField(Hardware, through="LinkJewelryHardware")
    strings = ManyToManyField(JewelryString, through="LinkJewelryJewelryString")
    packages = ManyToManyField(Package, through="LinkJewelryPackage")

    class Meta:
        verbose_name = _("Jewelry")
        verbose_name_plural = _("Jewelry")

    def __str__(self):
        return self.name

    def cost(self):
        cost = 0
        for linkjewelrybead in self.linkjewelrybead_set.all():
            cost += linkjewelrybead.bead.price * linkjewelrybead.quantity
        for linkjewelryhardware in self.linkjewelryhardware_set.all():
            cost += linkjewelryhardware.hardware.price * linkjewelryhardware.quantity
        for linkjewelryjewelrystring in self.linkjewelryjewelrystring_set.all():
            cost += (
                linkjewelryjewelrystring.jewelry_string.price
                * linkjewelryjewelrystring.quantity
            )
        for linkjewelrypackage in self.linkjewelrypackage_set.all():
            cost += linkjewelrypackage.package.price * linkjewelrypackage.quantity
        return cost


class LinkJewelryBead(Model):
    """
    Jewelry bead many to many model.
    """

    jewelry = ForeignKey(Jewelry, on_delete=PROTECT)
    bead = ForeignKey(Bead, on_delete=PROTECT, verbose_name=_("Bead"))
    quantity = PositiveIntegerField(verbose_name=_("Quantity"))

    class Meta:
        unique_together = ["jewelry", "bead"]
        verbose_name = _("Bead")
        verbose_name_plural = _("Beads")

    def __str__(self):
        return f"{self.jewelry.name} - {self.bead!s} * {self.quantity}"


class LinkJewelryHardware(Model):
    """
    Jewelry hardware many to many model.
    """

    jewelry = ForeignKey(Jewelry, on_delete=PROTECT)
    hardware = ForeignKey(Hardware, on_delete=PROTECT, verbose_name=_("Hardware"))
    quantity = PositiveIntegerField(verbose_name=_("Quantity"))
    is_main = BooleanField(
        null=False,
        verbose_name=_("Is Main?"),
    )  # included in the main body or not

    class Meta:
        unique_together = ["jewelry", "hardware"]
        verbose_name = _("Hardware")
        verbose_name_plural = _("Hardwares")

    def __str__(self):
        return f"{self.jewelry.name} - {self.hardware!s} * {self.quantity}"


class LinkJewelryJewelryString(Model):
    """
    Jewelry string many to many model.
    """

    jewelry = ForeignKey(Jewelry, on_delete=PROTECT)
    jewelry_string = ForeignKey(
        JewelryString,
        on_delete=PROTECT,
        verbose_name=_("Jewelry String"),
    )
    quantity = PositiveIntegerField(verbose_name=_("Quantity"))

    class Meta:
        verbose_name = _("Jewelry String")
        verbose_name_plural = _("Jewelry Strings")

    def __str__(self):
        return f"{self.jewelry.name} - {self.jewelry_string!s} * {self.quantity}mm"


class LinkJewelryPackage(Model):
    """
    Jewelry package many to many model.
    """

    jewelry = ForeignKey(Jewelry, on_delete=PROTECT)
    package = ForeignKey(
        Package,
        on_delete=PROTECT,
        verbose_name=_("Package"),
    )
    quantity = PositiveIntegerField(verbose_name=_("Quantity"))

    class Meta:
        verbose_name = _("Package")
        verbose_name_plural = _("Packages")

    def __str__(self):
        return f"{self.jewelry.name} - {self.package!s} * {self.quantity}"
