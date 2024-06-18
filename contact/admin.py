from import_export.admin import ImportExportModelAdmin
from django.contrib import admin 
from .resource import ReportResource  
from .models import Contact1

class ReportAdmin(ImportExportModelAdmin):
    resource_class = ReportResource     
    #list_display = ("id",'name',"imagen1")
    #search_fields = ('name',"imagen1")
    #list_filter = ('name',"imagen1") 

admin.site.register(Contact1, ReportAdmin)