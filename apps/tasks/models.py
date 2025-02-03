from django.db import models
from django.contrib.auth import get_user_model
from uuid import uuid4
from django.urls import reverse


User = get_user_model()

class Task(models.Model):
    STATUS_CHOICES  = (
        ('not_started', "Не начата"),
        ('started', 'Начата'),
        ('completed', 'Завершена'),
        ('reopened', 'Переоткрыта'),
    )
    uuid = models.UUIDField(default=uuid4, editable=False)
    name = models.CharField(max_length=128)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(auto_now=True, blank=True)
    date_updated = models.DateTimeField(auto_now=True, blank=True)
    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default= 'not_started'
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    executor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='executor' )
    priority = models.PositiveIntegerField()

    def get_absolute_url(self):
        return reverse('tasks:detail_task', args=[str(self.uuid)])

    def __str__(self):
        return f"Task: {self.name} -- {self.uuid}"

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['-priority']