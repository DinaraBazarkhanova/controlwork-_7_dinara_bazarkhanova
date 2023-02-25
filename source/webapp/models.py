from django.db import models
from django.db.models import TextChoices
from django.utils import timezone


# Create your models here.
class StatusChoice(TextChoices):
    ACTIVE = "active", "Активно"
    BLOCKED = "blocked", "Заблокировано"


class Article(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="Имя")
    email = models.EmailField(max_length=50, null=False, blank=True, verbose_name="Email")
    text = models.TextField(max_length=200, null=False, blank=False, verbose_name="Текст")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата и время обновления")
    status = models.CharField(max_length=20,
                              null=False,
                              blank=False,
                              choices=StatusChoice.choices,
                              default=StatusChoice.ACTIVE,
                              verbose_name="Статус"
                              )
    is_deleted = models.BooleanField(verbose_name='удалено', null=False, default=False)
    deleted_at = models.DateTimeField(verbose_name='Дата и время удаления', null=True, default=None)

    def __str__(self):
        return f"{self.name} - {self.status}"

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()
