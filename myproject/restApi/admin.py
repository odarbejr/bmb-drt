from django.contrib import admin

# Register your models here.
from .models import caveinventory
from .models import Period_accessment
from .models import Geographic_description
from .models import climatological_data
from .models import excisting_land_use
from .models import demographic_information
from .models import uses
from .models import Layers_attribute
from .models import cities


admin.site.register(Period_accessment)
admin.site.register(Geographic_description)
admin.site.register(climatological_data)
admin.site.register(excisting_land_use)
admin.site.register(demographic_information)
admin.site.register(uses)
admin.site.register(Layers_attribute)



class caveinventoryAdmin(admin.ModelAdmin):
    list_display = ("id", "cname", "region", "city", "barangay", "sitio_purok", "remark", "created_at", "updated_at")

admin.site.register(caveinventory, caveinventoryAdmin)

class citiesAdmin(admin.ModelAdmin):
    list_display = ("id", "code", "name", "region_id", "province_id", "city_id")

admin.site.register(cities, citiesAdmin)