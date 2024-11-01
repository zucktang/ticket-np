from Ticket.services.core import viewsets, permissions
from Ticket.apps.ticket.models import Ticket
from .serializers import TicketSerializer
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework import status

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
    }
    
    def get_queryset(self):
        return Ticket.objects.active()
    
    def destroy(self, request, *args, **kwargs):
        return Response({"error": "Tickets cannot be deleted."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    
    
    