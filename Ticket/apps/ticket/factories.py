import factory
from .models import Ticket

class TicketFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ticket

    title = factory.Faker('sentence')
    description = factory.Faker('paragraph')
    contact_info = factory.Faker('email')
    status = 'pending'
    


    