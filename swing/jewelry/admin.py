from pathlib import Path

from django.conf import settings
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.admin import TabularInline
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from swing.jewelry.models.bead import Bead
from swing.jewelry.models.bead import BeadMaterial
from swing.jewelry.models.bead import BeadShape
from swing.jewelry.models.bead import BeadShapeAttribute
from swing.jewelry.models.bead import LinkBeadBeadShapeAttribute
from swing.jewelry.models.color import Color
from swing.jewelry.models.hardware import Hardware
from swing.jewelry.models.hardware import HardwareMaterial
from swing.jewelry.models.hardware import HardwareType
from swing.jewelry.models.jewelry import Jewelry
from swing.jewelry.models.jewelry import JewelryType
from swing.jewelry.models.jewelry import LinkJewelryBead
from swing.jewelry.models.jewelry import LinkJewelryHardware
from swing.jewelry.models.jewelry import LinkJewelryJewelryString
from swing.jewelry.models.jewelry import LinkJewelryPackage
from swing.jewelry.models.jewelry import Series
from swing.jewelry.models.jewelry_string import JewelryString
from swing.jewelry.models.jewelry_string import JewelryStringType


class LinkJewelryBeadInline(TabularInline):
    model = LinkJewelryBead
    extra = 1  # 提供一个额外的空白表单


class LinkJewelryHardwareInline(TabularInline):
    model = LinkJewelryHardware
    extra = 1


class LinkJewelryJewelryStringInline(TabularInline):
    model = LinkJewelryJewelryString
    extra = 1


class LinkBeadBeadShapeAttributeInline(TabularInline):
    model = LinkBeadBeadShapeAttribute
    extra = 1


class LinkJewelryPackageInline(TabularInline):
    model = LinkJewelryPackage
    extra = 1


@admin.register(Jewelry)
class JewelryAdmin(ModelAdmin):
    inlines = [
        LinkJewelryBeadInline,
        LinkJewelryHardwareInline,
        LinkJewelryJewelryStringInline,
        LinkJewelryPackageInline,
    ]
    list_display = (
        "name",
        "series_link",
        "main_image",
        "design_image",
        "length",
        "get_cost",
        "price",
    )

    @admin.display(
        description=_("Series"),
    )
    def series_link(self, obj):
        return format_html(
            '<a href="{}">{}</a>',
            reverse("admin:jewelry_series_change", args=[str(obj.series.id)]),
            obj.series.name,
        )

    @admin.display(
        description=_("Cost"),
    )
    def get_cost(self, obj):
        return obj.cost()

    @admin.display(
        description=_("Main Image"),
    )
    def main_image(self, obj):
        return self.image(obj, f"{obj.series.name}/{obj.name}/产品图/02.导出/001.jpg")

    @admin.display(
        description=_("Design Image"),
    )
    def design_image(self, obj):
        return self.image(obj, f"{obj.series.name}/{obj.name}/设计图/02.导出/001.jpg")

    def image(self, obj, filepath):
        # 文件路径
        image_path = Path(settings.MEDIA_ROOT, filepath)
        # 使用相对路径生成URL
        image_url = Path(settings.MEDIA_URL, filepath)

        if Path.exists(image_path):
            html_content = render_to_string(
                Path(settings.APPS_DIR, "templates/jewelry/product_image.html"),
                {
                    "image_url": image_url,
                    "product": obj,
                },
            )

            return format_html(html_content)
        return "No Image"


@admin.register(Bead)
class BeadAdmin(ModelAdmin):
    inlines = [
        LinkBeadBeadShapeAttributeInline,
    ]


class JewelryInline(admin.TabularInline):
    model = Jewelry
    fields = ["view_link"]
    readonly_fields = ["view_link"]
    can_delete = False
    extra = 0

    @admin.display(
        description=_("Jewelry"),
    )
    def view_link(self, obj):
        return format_html(
            '<a href="{}">{}</a>',
            reverse("admin:jewelry_jewelry_change", args=[obj.id]),
            obj.name,
        )

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ("name", "view_jewelry")
    inlines = [JewelryInline]

    @admin.display(
        description=_("Jewelry"),
    )
    def view_jewelry(self, obj):
        jewelries = obj.jewelry_set.all()
        links = [
            format_html(
                '<a href="{}">{}</a>',
                reverse("admin:jewelry_jewelry_change", args=[jewelry.id]),
                jewelry.name,
            )
            for jewelry in jewelries
        ]
        return format_html(", ".join(links))


admin.site.register(BeadMaterial)
admin.site.register(BeadShape)
admin.site.register(BeadShapeAttribute)
admin.site.register(Color)
admin.site.register(Hardware)
admin.site.register(HardwareMaterial)
admin.site.register(HardwareType)
admin.site.register(JewelryString)
admin.site.register(JewelryStringType)
admin.site.register(JewelryType)
