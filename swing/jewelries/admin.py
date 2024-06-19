from django.contrib import admin

from swing.jewelries.models.bead import Bead
from swing.jewelries.models.bead import BeadMaterial
from swing.jewelries.models.hardware import Hardware
from swing.jewelries.models.hardware import HardwareMaterial
from swing.jewelries.models.hardware import HardwareType
from swing.jewelries.models.jewelry import Jewelry
from swing.jewelries.models.jewelry import JewelryType
from swing.jewelries.models.jewelry import Series
from swing.jewelries.models.jewelry_string import JewelryString

admin.site.register(Bead)
admin.site.register(BeadMaterial)
admin.site.register(Hardware)
admin.site.register(HardwareMaterial)
admin.site.register(HardwareType)
admin.site.register(JewelryString)
admin.site.register(Series)
admin.site.register(JewelryType)
admin.site.register(Jewelry)
