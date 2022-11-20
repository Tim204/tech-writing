from django.contrib import admin
from .models import Bird, BirdImages
from django.utils.html import format_html


class BirdImageInline(admin.TabularInline):
    model = BirdImages
    readonly_fields = ['thumbnail']

    def thumbnail(self, instance):
        if instance.bird_image.name != '':
            url = instance.data_sheet.url
            html = f'<img src="{url}" class="thumbnail">'
            return format_html(html)
        return ''


@admin.register(Bird)
class BirdAdmin(admin.ModelAdmin):
    inlines = [BirdImageInline]
    list_display = ['name', 'family']
