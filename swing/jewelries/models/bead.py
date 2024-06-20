from django.db.models import PROTECT
from django.db.models import CharField
from django.db.models import DecimalField
from django.db.models import ForeignKey
from django.db.models import Model
from django.db.models import URLField
from django.utils.translation import gettext_lazy as _


class BeadMaterial(Model):
    """
    Bead material model.
    """

    name = CharField(max_length=255, verbose_name=_("Name"))

    class Meta:
        verbose_name = _("Bead Material")
        verbose_name_plural = _("Bead Materials")

    def __str__(self):
        return self.name


class Bead(Model):
    """
    Bead model.
    """

    name = CharField(max_length=255, verbose_name=_("Name"))
    length = DecimalField(
        max_digits=10,
        decimal_places=1,
        verbose_name=_("Length"),
        help_text=_("The unit is millimeter."),
    )
    diameter = DecimalField(
        max_digits=10,
        decimal_places=1,
        verbose_name=_("Diameter"),
        help_text=_("The unit is millimeter."),
    )
    pore_diameter = DecimalField(
        max_digits=10,
        decimal_places=1,
        verbose_name=_("Pore Diameter"),
        help_text=_("The unit is millimeter."),
    )
    price = DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Price"))
    purcharse_link = URLField(
        blank=True,
        max_length=255,
        verbose_name=_("Purcharse Link"),
    )
    material = ForeignKey(BeadMaterial, on_delete=PROTECT, verbose_name=_("Material"))

    class Meta:
        verbose_name = _("Bead")
        verbose_name_plural = _("Beads")

    def __str__(self):
        return self.name
