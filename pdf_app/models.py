from django.db import models
from django.utils.translation import gettext_lazy as _
from celery import states
from django.contrib.auth import get_user_model

User = get_user_model()

ALL_STATES = sorted(states.ALL_STATES)
TASK_STATE_CHOICES = sorted(zip(ALL_STATES, ALL_STATES))


class Document(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=127, db_index=True, null=True, blank=True)
    data = models.TextField()
    status = models.CharField(
        max_length=50, default=states.PENDING, db_index=True,
        choices=TASK_STATE_CHOICES,
        verbose_name=_('Task State'),
        help_text=_('Current state of the task being run'))

    task_id = models.CharField(max_length=100, unique=True, db_index=True, null=True, blank=True)


    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)


    def __str__(self):
        return f'{ self.name }'