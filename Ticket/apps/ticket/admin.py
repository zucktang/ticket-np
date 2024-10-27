from django.contrib import admin

from .models import (
    Ticket, 
    TicketLog
)


class TicketLogInline(admin.TabularInline):
    model = TicketLog
    extra = 0

class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 
                    'contact_info', 'status', 'created', 'last_updated')
    search_fields = ('title', 'description', 'contact_info')
    list_filter = ('status', 'created', 'last_updated')
    inlines = [TicketLogInline]

admin.site.register(Ticket, TicketAdmin)

    