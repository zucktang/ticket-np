import factory
from Ticket.apps.ticket.models import Ticket
from django.utils import timezone

class TicketFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ticket

    title = factory.Sequence(lambda n: f"Test Ticket {n}")
    description = "A test ticket description"
    contact_info = "contact@example.com"
    status = "pending"
    start_date = timezone.now().date()
    expire_date = factory.LazyFunction(lambda: timezone.now().date())
    
