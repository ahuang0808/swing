from django.db.models import CharField
from django.db.models import DecimalField
from django.db.models import Model
from django.db.models import URLField
from django.utils.translation import gettext_lazy as _


class Package(Model):
    """
    Color model.
    """

    name = CharField(max_length=255, verbose_name=_("Name"))
    price = DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Price"))
    purchase_link = URLField(
        blank=True,
        max_length=255,
        verbose_name=_("Purchase Link"),
    )

    class Meta:
        verbose_name = _("Package")
        verbose_name_plural = _("Packages")

    def __str__(self):
        return self.name
