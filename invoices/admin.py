from django.contrib import admin

# Register your models here.
from .models import Invoice, Item

admin.site.register(Invoice)
admin.site.register(Item)
