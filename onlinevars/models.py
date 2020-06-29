import uuid
from django.db import models
from django.utils import timezone
from datetime import timedelta
from random import randint

# Create your models here.

class Variable(models.Model):
    name = models.CharField("Name", max_length=100, primary_key=True)
    value = models.CharField("Wert", max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name
    __str__.short_description = "Variable"

    class Meta:
        verbose_name = "Variable"
        verbose_name_plural = "Variablen"
