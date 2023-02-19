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
    tag = TaggableManager(blank=True)

    def __str__(self):
        return f'{self.user.username} - Quetion'
    

    def get_absolute_url(self):
        return reverse('question_blueprint:question_view')


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name="answer", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=10000)
    created_date = models.DateTimeField(default=timezone.now)

    # class Meta:
    #     ordering = ['-created_date']

    def __str__(self):
        return f"{self.question.title}-{self.question.user}"
    
    def get_absolute_url(self):
        return reverse('question_blueprint:question_detail_view', kwargs={'pk':self.pk})
    

    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)



class Upvote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_vote')
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='answer_vote')


    