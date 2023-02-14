from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
# CRUD functionalities

class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return f'{self.user.username} - Quetion'
    


