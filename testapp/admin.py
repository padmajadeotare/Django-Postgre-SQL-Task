from django.contrib import admin
from testapp.models import Info
# Register your models here.
class InfoAdmin(admin.ModelAdmin):
    list_display=['id','first_name','last_name']

admin.site.register(Info,InfoAdmin)
