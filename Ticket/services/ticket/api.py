from Ticket.services.core import viewsets, permissions
from Ticket.apps.ticket.models import Ticket
from .serializers import TicketSerializer
from rest_framework.authentication import TokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['title', 'description', 'contact_info', 'status']
    search_fields = ['title', 'description', 'contact_info', 'status']
    ACTION_SERIALIZERS = {
        'list': TicketSerializer, 
        'retrieve': TicketSerializer,
        'create': TicketSerializer,
        'update': TicketSerializer,
        'partial_update': TicketSerializer,
        'destroy': TicketSerializer,
    }
    