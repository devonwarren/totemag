from django.contrib import admin
from articles import models


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'publisher', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')

admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Category, CategoryAdmin)
