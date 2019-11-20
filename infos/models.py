from django.db import models

# Create your models here.
class SystemMessage(models.Model):
    message = models.CharField(max_length=200)

    def __str__(self):
        return self.message