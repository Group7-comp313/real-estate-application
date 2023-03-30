from django.contrib import admin
from realtors.models import Realtor

class RealtorAdmin(admin.ModelAdmin):
   list_display = ['name','email']
   list_display_links = ['name','email']


admin.site.register(Realtor,RealtorAdmin)

# Register your models here.
