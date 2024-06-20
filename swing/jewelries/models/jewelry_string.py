from django.db.models import CharField
from django.db.models import Model
from django.db.models import PositiveIntegerField
from django.db.models import URLField
from django.utils.translation import gettext_lazy as _


class JewelryString(Model):
    """
    Jewelry string model.
    """

    name = CharField(max_length=255, verbose_name=_("Name"))
    price = PositiveIntegerField(
        verbose_name=_("Price"),
        help_text=_("Price per mm"),
    )  # per mm
    purcharse_link = URLField(
        blank=True,
        max_length=255,
        verbose_name=_("Purcharse Link"),
    )

    class Meta:
        verbose_name = _("Jewelry String")
        verbose_name_plural = _("Jewelry Strings")

    def __str__(self):
        return self.name
