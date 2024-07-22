from django.contrib import admin
from .models import Cliente, Pais, Region, Comuna
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Pais)
admin.site.register(Region)
admin.site.register(Comuna)
