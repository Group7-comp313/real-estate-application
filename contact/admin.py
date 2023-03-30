from django.contrib import admin
from .models import  Contact
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','listing','name','email']
    list_display_links = ["name","id"]
    search_fields = ["name","email"]
    list_per_page = 25

admin.site.register(Contact,ContactAdmin)

# Register your models here.
