from django.contrib import admin
from month.models import Theme, ThemeArticle


class ThemeArticleInline(admin.StackedInline):
    verbose_name = 'Theme Articles'
    model = ThemeArticle
    extra = 1
    max_num = 4


class ThemeAdmin(admin.ModelAdmin):
    verbose_name = 'Themes'
    list_display = ('title', 'year', 'month')
    inlines = [
        ThemeArticleInline,
    ]


admin.site.register(Theme, ThemeAdmin)
