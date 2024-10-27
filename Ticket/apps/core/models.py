import uuid
from django.db import models
from django.core.exceptions import ImproperlyConfigured

            
class BaseModel(models.Model):

    created = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )
    last_updated = models.DateTimeField(
        auto_now=True,
        editable=False
    )

    class Meta:
        abstract = True
            
    @classmethod
    def create(cls, **kwargs):
        instance = cls(**kwargs)
        instance.save()
        return instance
    
    def update(self, save=False, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        if save:
            self.save()
            
    