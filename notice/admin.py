from django.contrib import admin
from .models import Notice


class NoticeAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'author', 'create', 'like',)


admin.site.register(Notice, NoticeAdmin)
