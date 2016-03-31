from django.contrib import admin
from ads import models


class AdImageAdmin(admin.ModelAdmin):
    list_display = ('url', 'published', 'caption',)


admin.site.register(models.HeaderAdImage, AdImageAdmin)
admin.site.register(models.SideAdImage, AdImageAdmin)
