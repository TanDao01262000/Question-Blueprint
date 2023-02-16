from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.urls import reverse
# Create your models here.
# CRUD functionalities

class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    tag = TaggableManager()

    def __str__(self):
        return f'{self.user.username} - Quetion'
    

    def get_absolute_url(self):
        return reverse('question_blueprint:question_view')

