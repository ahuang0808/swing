from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.admin import TabularInline

from swing.jewelries.models.bead import Bead
from swing.jewelries.models.bead import BeadMaterial
from swing.jewelries.models.hardware import Hardware
from swing.jewelries.models.hardware import HardwareMaterial
from swing.jewelries.models.hardware import HardwareType
from swing.jewelries.models.jewelry import Jewelry
from swing.jewelries.models.jewelry import JewelryType
from swing.jewelries.models.jewelry import LinkJewelryBead
from swing.jewelries.models.jewelry import LinkJewelryHardware
from swing.jewelries.models.jewelry import LinkJewelryJewelryString
from swing.jewelries.models.jewelry import Series
from swing.jewelries.models.jewelry_string import JewelryString


class LinkJewelryBeadInline(TabularInline):
    model = LinkJewelryBead
    extra = 1  # 提供一个额外的空白表单


class LinkJewelryHardwareInline(TabularInline):
    model = LinkJewelryHardware
    extra = 1


class LinkJewelryJewelryStringInline(TabularInline):
    model = LinkJewelryJewelryString
    extra = 1


@admin.register(Jewelry)
class JewelryAdmin(ModelAdmin):
    inlines = [
        LinkJewelryBeadInline,
        LinkJewelryHardwareInline,
        LinkJewelryJewelryStringInline,
    ]
    list_display = ("name", "get_length", "get_price")

    @admin.display(
        description="Length",
    )
    def get_length(self, obj):
        return obj.length()

    @admin.display(
        description="Price",
    )
    def get_price(self, obj):
        return obj.price()


admin.site.register(Bead)
admin.site.register(BeadMaterial)
admin.site.register(Hardware)
admin.site.register(HardwareMaterial)
admin.site.register(HardwareType)
admin.site.register(JewelryString)
admin.site.register(Series)
admin.site.register(JewelryType)
