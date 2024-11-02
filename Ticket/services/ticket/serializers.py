from rest_framework import serializers
from Ticket.apps.ticket.models import Ticket, TicketLog

class TicketLogSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TicketLog
        fields = ['action', 'previous_status', 'new_status', 'created', 'last_updated']

class TicketSerializer(serializers.ModelSerializer):
    logs = TicketLogSerializer(many=True, read_only=True)

    class Meta:
        model = Ticket
        fields = '__all__'