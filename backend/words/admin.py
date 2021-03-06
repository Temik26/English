from django.contrib import admin
from .models import (Topic, Unit, Dictionary,
                     Translation, TranslationType)


class TranslationInline(admin.StackedInline):
    model = Translation
    extra = 1


@admin.register(Dictionary)
class DictionaryAdmin(admin.ModelAdmin):
    inlines = [
        TranslationInline,
    ]


admin.site.site_header = 'English'
admin.site.register(Topic)
admin.site.register(Unit)
admin.site.register(TranslationType)
admin.site.site_url = None

