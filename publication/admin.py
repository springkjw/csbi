from django.contrib import admin
from .models import Publication, PublicationItem


class PublicationItemInline(admin.TabularInline):
    model = PublicationItem


class PublicationAdmin(admin.ModelAdmin):
    inlines = [
        PublicationItemInline
    ]

    class Meta:
        model = Publication


admin.site.register(Publication, PublicationAdmin)
