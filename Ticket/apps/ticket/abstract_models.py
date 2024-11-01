import uuid

from django.utils import timezone
from django.db import models

from ..core.models import BaseModel

class Status:
    PENDING = 'pending'
    ACCEPTED = 'accepted'
    RESOLVED = 'resolved'
    REJECTED = 'rejected'
    
    
    status_choices = [
        (PENDING, 'รอดำเนินการ'),
        (ACCEPTED, 'รับเรื่องแล้ว'),
        (RESOLVED, 'ดำเนินการแก้ไขแล้ว'),
        (REJECTED, 'ถูกปฏิเสธ')
    ]
    

class AbstractTicket(BaseModel):
    def auto_generate_id():
        now = timezone.now()
        prefix = now.strftime('%y%m%d')
        timestamp = now.timestamp()
        timestamp = str(timestamp).split('.')
        random = uuid.uuid4().hex[:8].upper()
        return 'TICK' + prefix + timestamp[0][:4] + random + timestamp[1][:5]
    
    id = models.CharField(
        primary_key=True,
        default=auto_generate_id,
        max_length=35,
        editable=False,
    )
    image = models.ImageField(
        upload_to='ticket_images/', 
        null=True, 
        blank=True
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    contact_info = models.CharField(max_length=255)
    status = models.CharField(
        choices=Status.status_choices, 
        default=Status.PENDING, 
        max_length=50
    )
    expire_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        abstract = True
        verbose_name = 'ตั๋ว'
        verbose_name_plural = 'ตั๋ว'
        
        
class AbstractTicketLog(BaseModel):
    ticket = models.ForeignKey(
        'ticket.Ticket', 
        on_delete=models.CASCADE, 
        related_name='logs'
    )
    action = models.CharField(max_length=255)
    previous_status = models.CharField(max_length=50, null=True, blank=True)
    new_status = models.CharField(max_length=50, null=True, blank=True)
    
    class Meta:
        abstract = True
        ordering = ['-created']
    
    def __str__(self):
        return f"Log for {self.ticket.title} at {self.last_updated}"  
    
    