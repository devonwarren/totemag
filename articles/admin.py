from django.contrib import admin
from articles.models import Article, SlideshowImage, Category


class SlideshowInline(admin.StackedInline):
    model = SlideshowImage
    extra = 0


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'publisher', 'category')
    inlines = [SlideshowInline]
    exclude = ['slideshow_images', ]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
