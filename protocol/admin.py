from django.contrib import admin
from .models import Protocol, ProtocolPresenter


class PresenterInline(admin.TabularInline):
    model = ProtocolPresenter
    extra = 0


class ProtocolAdmin(admin.ModelAdmin):
    inlines = [PresenterInline, ]

    list_display = ('__unicode__', 'type', 'presenter',)

    def presenter(self, obj):
        p = ProtocolPresenter.objects.filter(protocol=obj)
        presenter = ''
        for item in p:
            presenter += str(item)

        return presenter


admin.site.register(Protocol, ProtocolAdmin)
