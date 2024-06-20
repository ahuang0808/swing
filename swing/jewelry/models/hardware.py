from django.db.models import PROTECT
from django.db.models import CharField
from django.db.models import DecimalField
from django.db.models import ForeignKey
from django.db.models import Model
from django.db.models import URLField
from django.utils.translation import gettext_lazy as _

from swing.jewelry.models.color import Color


class HardwareType(Model):
    """
    Hardware type model.
    """

    name = CharField(max_length=255, verbose_name=_("Name"))

    class Meta:
        verbose_name = _("Hardware Type")
        verbose_name_plural = _("Hardware Types")

    def __str__(self):
        return self.name


class HardwareMaterial(Model):
    """
    Hardware material model.
    """

    name = CharField(max_length=255, verbose_name=_("Name"))

    class Meta:
        verbose_name = _("Hardware Material")
        verbose_name_plural = _("Hardware Materials")

    def __str__(self):
        return self.name


class Hardware(Model):
    """
    Hardware model.
    """

    length = DecimalField(
        max_digits=10,
        decimal_places=1,
        verbose_name=_("Length"),
        help_text=_("The unit is millimeter."),
    )
    width = DecimalField(
        max_digits=10,
        decimal_places=1,
        verbose_name=_("Width"),
        help_text=_("The unit is millimeter."),
    )
    color = ForeignKey(Color, on_delete=PROTECT, verbose_name=_("Color"))
    type = ForeignKey(HardwareType, on_delete=PROTECT, verbose_name=_("Type"))
    price = DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Price"))
    purcharse_link = URLField(
        blank=True,
        max_length=255,
        verbose_name=_("Purcharse Link"),
    )
    material = ForeignKey(
        HardwareMaterial,
        on_delete=PROTECT,
        verbose_name=_("Material"),
    )

    class Meta:
        verbose_name = _("Hardware")
        verbose_name_plural = _("Hardwares")

    def __str__(self):
        return f"{self.color} {self.material} {self.type}"
