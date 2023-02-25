from django.db import models
from django.db.models import TextChoices


# Create your models here.
class StatusChoice(TextChoices):
    ACTIVE = "active", "Active"
    BLOCKED = "blocked", "Blocked"


class Article(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="Name")
    email = models.EmailField(max_length=50, null=False, blank=True, verbose_name="Email")
    text = models.TextField(max_length=200, null=False, blank=False, verbose_name="Text")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creation date and time")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated date and time")
    status = models.CharField(max_length=20,
                              null=False,
                              blank=False,
                              choices=StatusChoice.choices,
                              default=StatusChoice.ACTIVE,
                              verbose_name="Status"
                              )

    def __str__(self):
        return f"{self.name} - {self.status}"
