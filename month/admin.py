from django.contrib import admin
from month.models import Theme, ThemeArticle


class ThemeArticleInline(admin.StackedInline):
    verbose_name = 'Theme Articles'
    model = ThemeArticle
    extra = 1


class ThemeAdmin(admin.ModelAdmin):
    verbose_name = 'Themes'
    list_display = ('title', 'year', 'month')
    inlines = [
        ThemeArticleInline,
    ]
    max_num = 4


admin.site.register(Theme, ThemeAdmin)
