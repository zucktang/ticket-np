from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from Ticket.apps.ticket.models import Ticket
from Ticket.apps.ticket.factories import TicketFactory
from ..serializers import TicketSerializer

class TicketViewSetTests(APITestCase):
    def setUp(self):
        self.ticket = TicketFactory()
        self.url = reverse('ticket-list')

    def test_001_ticket_list(self):
        response = self.client.get(self.url)
        tickets = Ticket.objects.all()
        serializer = TicketSerializer(tickets, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_002_ticket_create(self):
        data = {
            "title": "New Ticket",
            "description": "New ticket description",
            "contact_info": "newcontact@example.com",
            "status": "pending"
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Ticket.objects.filter(title="New Ticket").exists())

    def test_003_ticket_retrieve(self):
        url = reverse('ticket-detail', args=[self.ticket.id])
        response = self.client.get(url)
        serializer = TicketSerializer(self.ticket)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_004_ticket_update(self):
        url = reverse('ticket-detail', args=[self.ticket.id])
        data = {"status": "accepted"}
        response = self.client.patch(url, data)
        self.ticket.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.ticket.status, "accepted")

    def test_005_ticket_delete_not_allowed(self):
        url = reverse('ticket-detail', args=[self.ticket.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertTrue(Ticket.objects.filter(id=self.ticket.id).exists())