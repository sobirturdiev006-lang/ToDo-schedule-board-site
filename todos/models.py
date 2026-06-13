from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from .constants import TODO

class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=7, default='#6366f1')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


User = get_user_model()

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')
    status = models.IntegerField(choices=TODO.STATUS.Constants,default=0)
    priority = models.IntegerField(max_length=10, choices=TODO.PRIORITY.PRIORITY_CHOICES, default=1)
    title = models.CharField(max_length=255)
    deadline = models.DateTimeField(null=True, blank=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='todos')
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-priority']

    def __str__(self):
        return self.title
