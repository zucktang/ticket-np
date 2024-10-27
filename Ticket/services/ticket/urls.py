from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import (
   TicketViewSet
)

router = DefaultRouter()
router.register(r'', TicketViewSet)


urlpatterns = [
    path('', include(router.urls)),
]