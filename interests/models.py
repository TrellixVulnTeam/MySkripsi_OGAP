from django.db import models

class Interest(models.Model):
    name = models.CharField(max_length=20, blank=False)

    class Meta:
        ordering = ['id']