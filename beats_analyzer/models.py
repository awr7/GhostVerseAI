from django.db import models

# Create your models here.
class Beat(models.Model):
    file = models.FileField(upload_to='beats/')