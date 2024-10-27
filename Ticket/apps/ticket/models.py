from .abstract_models import (
    AbstractTicket,
    AbstractTicketLog
)
from django.db import models


class Ticket(AbstractTicket):
    pass


class TicketLog(AbstractTicketLog):
    pass
