from django.db.models import PROTECT
from django.db.models import CharField
from django.db.models import DecimalField
from django.db.models import ForeignKey
from django.db.models import ManyToManyField
from django.db.models import Model
from django.db.models import URLField
from django.utils.translation import gettext_lazy as _

from swing.jewelry.models.color import Color


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


class BeadShape(Model):
    """
    Bead shape model.
    """

    name = CharField(max_length=255, verbose_name=_("Name"))

    class Meta:
        verbose_name = _("Bead Shape")
        verbose_name_plural = _("Bead Shapes")

    def __str__(self):
        return self.name


class BeadShapeAttribute(Model):
    """
    Bead shape attribute model.
    """

    name = CharField(max_length=255, verbose_name=_("Name"))

    class Meta:
        verbose_name = _("Bead Shape Attribute")
        verbose_name_plural = _("Bead Shape Attributes")

    def __str__(self):
        return self.name


class Bead(Model):
    """
    Bead model.
    """

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
    color = ForeignKey(Color, on_delete=PROTECT, verbose_name=_("Color"))
    price = DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Price"))
    purcharse_link = URLField(
        blank=True,
        max_length=255,
        verbose_name=_("Purcharse Link"),
    )
    bead_shape_attributes = ManyToManyField(
        BeadShapeAttribute,
        through="LinkBeadBeadShapeAttribute",
    )
    shape = ForeignKey(BeadShape, on_delete=PROTECT, verbose_name=_("Shape"))
    material = ForeignKey(BeadMaterial, on_delete=PROTECT, verbose_name=_("Material"))

    class Meta:
        verbose_name = _("Bead")
        verbose_name_plural = _("Beads")

    def __str__(self):
        attributes_list = []
        for linkbeadbeadattribute in self.linkbeadbeadattribute_set.all():
            attributes_list += linkbeadbeadattribute.bead_shape_attribute.name
        return f"{self.color} {self.material} {" ".join(attributes_list)} {self.shape}"


class LinkBeadBeadShapeAttribute(Model):
    """
    Bead Bead Shape Attribute many to many model.
    """

    bead = ForeignKey(Bead, on_delete=PROTECT)
    bead_shape_attribute = ForeignKey(
        BeadShapeAttribute,
        on_delete=PROTECT,
        verbose_name=_("Bead Shape Attribute"),
    )

    class Meta:
        unique_together = ["bead", "bead_shape_attribute"]
        verbose_name = _("Bead Shape Attribute")
        verbose_name_plural = _("Bead Shape Attributes")

    def __str__(self):
        return f"{self.bead!s} - {self.bead_shape_attribute.name}"
