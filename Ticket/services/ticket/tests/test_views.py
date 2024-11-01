from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from Ticket.apps.ticket.models import Ticket
from Ticket.apps.ticket.factories import TicketFactory
from ..serializers import TicketSerializer
from django.utils import timezone
from datetime import timedelta

class TicketViewSetTests(APITestCase):
    def setUp(self):
        self.active_ticket = TicketFactory(
            expire_date=timezone.now() + timedelta(days=30)
        )
        
        self.expired_ticket = TicketFactory(
            expire_date=timezone.now() - timedelta(days=1)
        )
        self.url = reverse('ticket-list')

    def test_001_ticket_list_active_tickets_only(self):
        response = self.client.get(self.url)
        tickets = Ticket.objects.active()
        serializer = TicketSerializer(tickets, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
        self.assertIn(self.active_ticket.id, [ticket['id'] for ticket in response.data])
        self.assertNotIn(self.expired_ticket.id, [ticket['id'] for ticket in response.data])

    def test_002_ticket_create(self):
        data = {
            "title": "New Ticket",
            "description": "New ticket description",
            "contact_info": "newcontact@example.com",
            "status": "pending",
            "expire_date": (timezone.now() + timedelta(days=15)).date()
        }
        response = self.client.post(self.url, data)
        id = response.data.get('id')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Ticket.objects.filter(pk=id).exists())

    def test_003_ticket_retrieve(self):
        url = reverse('ticket-detail', args=[self.active_ticket.id])
        response = self.client.get(url)
        serializer = TicketSerializer(self.active_ticket)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_004_ticket_update(self):
        url = reverse('ticket-detail', args=[self.active_ticket.id])
        data = {"status": "accepted"} 
        response = self.client.patch(url, data)
        self.active_ticket.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.active_ticket.status, "accepted")

    def test_005_ticket_delete_not_allowed(self):
        url = reverse('ticket-detail', args=[self.active_ticket.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertTrue(Ticket.objects.filter(id=self.active_ticket.id).exists())

    def test_006_create_ticket_with_expired_date(self):
        data = {
            "title": "Expired Ticket",
            "description": "This ticket is expired.",
            "contact_info": "expired@example.com",
            "status": "pending",
            "expire_date": (timezone.now() - timedelta(days=1)).date()
        }
        response = self.client.post(self.url, data)
        id = response.data.get('id')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Ticket.objects.filter(pk=id).exists())