from django.shortcuts import get_object_or_404

from .models import Task
from apps.accounts.models import Profile
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, post_delete
from django.dispatch import  receiver

User = get_user_model()

@receiver(post_save, sender=Task)
def create_task(sender, instance, created, **kwargs):
    profile = get_object_or_404(Profile, user=instance.executor)
    if created:
        profile.tasks_active += 1

    else:
        if instance.status == 'completed':
            profile.tasks_completed += 1
            profile.tasks_active -= 1

    profile.save()


@receiver(post_delete, sender=Task)
def delete_tesk(sender, instance, *args, **kwargs):
    profile = get_object_or_404(Profile, user=instance.executor)
    if profile.tasks_active > 0:
        profile.tasks_active -= 1

    profile.save()