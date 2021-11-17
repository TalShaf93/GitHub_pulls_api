from django.db import models

# Create your models here.

class Pull_request(models.Model):
    pull_request_id = models.IntegerField()
    number = models.IntegerField()
    url = models.URLField()
    state = models.CharField(max_length=100)
    locked = models.BooleanField()
    title = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    is_admin = models.BooleanField()
    body = models.CharField(max_length=500)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    closed_at = models.DateTimeField()
    merged_at = models.DateTimeField()