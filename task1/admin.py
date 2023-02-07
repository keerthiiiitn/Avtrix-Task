from django.contrib import admin
from.models import Food
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class FoodAdmin(ImportExportModelAdmin):
    list_display = ['OrderDate','Region','City','Category','Product','Quantity','UnitPrice']

admin.site.register(Food,FoodAdmin)