from django.db.models import CharField
from django.db.models import Model
from django.utils.translation import gettext_lazy as _


class Color(Model):
    """
    Color model.
    """

    name = CharField(max_length=255, verbose_name=_("Name"))

    class Meta:
        verbose_name = _("Color")
        verbose_name_plural = _("Colors")

    def __str__(self):
        return self.name
