from django.apps import AppConfig


class TicketConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Ticket.apps.ticket'
    
    def ready(self):
        import Ticket.apps.ticket.signals
