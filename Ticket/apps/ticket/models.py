from .abstract_models import (
    AbstractTicket,
    AbstractTicketLog
)
from django.utils import timezone
from django.db import models



class Ticket(AbstractTicket):
    def is_expired(self):
        return self.expire_date and self.expire_date < timezone.now().date()
    
    def delete(self, *args, **kwargs):
        raise NotImplementedError("Tickets cannot be deleted once created.")


class TicketLog(AbstractTicketLog):
    pass
