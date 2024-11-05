from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Ticket, TicketLog

def log_change(ticket, action, **extra_fields):
    TicketLog.objects.create(ticket=ticket, action=action, **extra_fields)

@receiver(post_save, sender=Ticket)
def log_ticket_creation(sender, instance, created, **kwargs):
    if created:
        log_change(instance, "Ticket created")

@receiver(pre_save, sender=Ticket)
def log_ticket_updates(sender, instance, **kwargs):
    if instance.pk:
        previous_ticket = Ticket.objects.get(pk=instance.pk)

        if previous_ticket.status != instance.status:
            log_change(instance, "Status changed",
                       previous_status=previous_ticket.status,
                       new_status=instance.status)

        if previous_ticket.description != instance.description:
            log_change(instance, "Description updated")

        if previous_ticket.contact_info != instance.contact_info:
            log_change(instance, "Contact information updated")
