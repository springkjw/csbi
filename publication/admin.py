from django.contrib import admin
from .models import Publication, PublicationItem


class PublicationItemInline(admin.TabularInline):
    model = PublicationItem

    raw_id_fields = ('name',)
    extra = 1

class PublicationAdmin(admin.ModelAdmin):
    inlines = [
        PublicationItemInline
    ]

    class Meta:
        model = Publication


admin.site.register(Publication, PublicationAdmin)
