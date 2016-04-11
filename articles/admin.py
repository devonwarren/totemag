from django.contrib import admin
from articles.models import Article, SlideshowImage, Category


class SlideshowInline(admin.StackedInline):
    model = SlideshowImage
    extra = 0


class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'published', 'published_date', 'publisher', 'category')
    search_fields = ['title', ]
    list_filter = ('published', 'category')
    inlines = [SlideshowInline]
    exclude = ['slideshow_images', ]
    fieldsets = (
        (None, {
            'fields': (
                'title', 'published', 'image', 'image_attribution',
                'body', 'category', 'published_date', 'publisher')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': (
                'publish_after', 'count'),
        }),
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
