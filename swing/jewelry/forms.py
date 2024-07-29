from django import forms
from django.utils.translation import gettext_lazy as _

from swing.jewelry.models.jewelry import Jewelry


class JewelryForm(forms.ModelForm):
    cost = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        label=_("Cost"),
        help_text=_("Automatic calculation, no manual input required."),
        required=False,
        widget=forms.TextInput(attrs={"readonly": "readonly"}),
    )

    class Meta:
        model = Jewelry
        fields = "__all__"  # noqa: DJ007

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Populate the custom field with the desired value
        if self.instance and self.instance.pk:
            self.fields["cost"].initial = self.instance.cost
