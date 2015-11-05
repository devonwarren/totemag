from django.contrib import admin
from articles import models


class SlideshowInline(admin.TabularInline):
    model = models.Article.slideshow_images.through


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'publisher', 'category')
    inlines = [SlideshowInline, ]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')

admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Category, CategoryAdmin)
