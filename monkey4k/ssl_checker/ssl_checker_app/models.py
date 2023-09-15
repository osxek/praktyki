from django.db import models
from django.utils import timezone

class SSLCertificate(models.Model):
    id = models.AutoField(primary_key=True)
    domain = models.CharField(max_length=255)
    valid_until = models.DateField()
    created_at = models.DateTimeField(default=timezone.now)

class Video(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.domain

