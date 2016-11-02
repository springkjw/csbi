from django.contrib import admin
from .models import Notice


class NoticeAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'type', 'created', 'like',)


admin.site.register(Notice, NoticeAdmin)
