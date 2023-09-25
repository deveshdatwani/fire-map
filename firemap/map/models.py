import uuid
from django.db import models

# Create your models here.

class Fire(models.Model):
    idx = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    img = models.ImageField(null=True)   

    def __str__(self):
        return f'{self.idx}'
