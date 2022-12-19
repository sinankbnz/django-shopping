from django.contrib import admin
from . models import Product

class productAdmin(admin.ModelAdmin):
    list_display=('name','price')

admin.site.register(Product,productAdmin)