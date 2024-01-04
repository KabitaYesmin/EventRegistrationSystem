from django.db import models


class Events(models.Model):
    objects=None
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=False, blank=True)
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "system_dt"
