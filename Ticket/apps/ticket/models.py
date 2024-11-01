from .abstract_models import (
    AbstractTicket,
    AbstractTicketLog
)
from django.utils import timezone
from django.db import models
from django.conf import settings


class TicketQuerySet(models.QuerySet):
    def active(self):
        return self.filter(expire_date__gt=timezone.now())

class TicketManager(models.Manager):
    def get_queryset(self):
        return TicketQuerySet(self.model, using=self._db)

    def active(self):
        return self.get_queryset().active()

class Ticket(AbstractTicket):
    objects = TicketManager()
    
    def is_expired(self):
        return self.expire_date and self.expire_date < timezone.now().date()
    
    def delete(self, *args, **kwargs):
        raise NotImplementedError("Tickets cannot be deleted once created.")
    
    def save(self, *args, **kwargs):
        if self.pk is None:
            self.expire_date = timezone.now().date() + timezone.timedelta(days=settings.EXPIRE_DAYS)
        super().save(*args, **kwargs)


class TicketLog(AbstractTicketLog):
    pass
