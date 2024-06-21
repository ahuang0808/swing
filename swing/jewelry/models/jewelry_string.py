from django.db.models import PROTECT
from django.db.models import CharField
from django.db.models import DecimalField
from django.db.models import ForeignKey
from django.db.models import Model
from django.db.models import URLField
from django.utils.translation import gettext_lazy as _

from swing.jewelry.models.color import Color


class JewelryStringType(Model):
    """
    Jewelry String type model.
    """

    name = CharField(max_length=255, verbose_name=_("Name"))

    class Meta:
        verbose_name = _("Jewelry String Type")
        verbose_name_plural = _("Jewelry String Types")

    def __str__(self):
        return self.name


class JewelryString(Model):
    """
    Jewelry string model.
    """

    type = ForeignKey(JewelryStringType, on_delete=PROTECT, verbose_name=_("Type"))
    diameter = DecimalField(
        max_digits=10,
        decimal_places=1,
        verbose_name=_("Diameter"),
        help_text=_("The unit is millimeter."),
    )
    color = ForeignKey(Color, on_delete=PROTECT, verbose_name=_("Color"))
    price = DecimalField(
        max_digits=10,
        decimal_places=3,
        verbose_name=_("Price"),
        help_text=_("Price per mm"),
    )  # per mm
    purchase_link = URLField(
        blank=True,
        max_length=255,
        verbose_name=_("Purchase Link"),
    )

    class Meta:
        verbose_name = _("Jewelry String")
        verbose_name_plural = _("Jewelry Strings")

    def __str__(self):
        return f"{self.color} {self.type}"
