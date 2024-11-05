from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Ticket, TicketLog

@receiver(post_save, sender=Ticket)
def log_ticket_changes(sender, instance, created, **kwargs):
    if created:
        TicketLog.objects.create(
            ticket=instance,
            action="Ticket created",
        )


@receiver(pre_save, sender=Ticket)
def update_ticket_status(sender, instance, **kwargs):
    previous_ticket = Ticket.objects.get(pk=instance.pk)
    if previous_ticket.status != instance.status:
        TicketLog.objects.create(
            ticket=instance,
            action="Status changed",
            previous_status=previous_ticket.status,
            new_status=instance.status,
        )

    if previous_ticket.description != instance.description:
        TicketLog.objects.create(
            ticket=instance,
            action="Description updated",
        )

    if previous_ticket.contact_info != instance.contact_info:
        TicketLog.objects.create(
            ticket=instance,
            action="Contact information updated",
        )
