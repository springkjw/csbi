from django.contrib import admin
from .models import Publication, PublicationItem


class PublicationItemInline(admin.TabularInline):
    model = PublicationItem
    extra = 1

class PublicationAdmin(admin.ModelAdmin):
    inlines = [
        PublicationItemInline
    ]

    list_display = ('__unicode__', 'type',)

    class Meta:
        model = Publication


admin.site.register(Publication, PublicationAdmin)
