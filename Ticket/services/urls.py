from django.conf import settings
from django.urls import path, include

urlpatterns = [
    path(r'ticket/', include('Ticket.services.ticket.urls')),
]