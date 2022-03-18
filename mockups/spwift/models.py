from django.db import models

class SpecifyUser(models.Model):
    # userid = models.SmallIntegerField(db_index=True, null=False, blank=False)
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    password = models.CharField(max_length=255)
