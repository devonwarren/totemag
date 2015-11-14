from django.contrib import admin
from staff import models


class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'featured')

admin.site.register(models.Staff, StaffAdmin)
