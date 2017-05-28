from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Question - вопрос
#title - заголовок вопроса
#text - полный текст вопроса
#added_at - дата добавления вопроса
#rating - рейтинг вопроса (число)
#author - автор вопроса
#likes - список пользователей, поставивших "лайк"
class QuestionManager(models.Manager):      
    def new(self):
        return Question.objects.order_by('-added_at')

    def popular(self):
        return Question.objects.order_by('-rating')

class Question(models.Model):

    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
	rating = models.IntegerField(default=0)
	author = models.ForeignKey(User, related_name="question_author")
	likes = models.ManyToManyField(User, related_name="question_likes", blank=True)
	objects = QuestionManager()
	
    def get_absolute_url(self):
        return '/question/%d/' % self.pk

    class Meta:
        db_table = 'qaQuestions'
        ordering = ['-added_at']

#Answer - ответ
#text - текст ответа
#added_at - дата добавления ответа
#question - вопрос, к которому относится ответ
#author - автор ответа
class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
	question = models.ForeignKey(Question)
	author = models.ForeignKey(User)
	
    class Meta:
        db_table = 'qaAnswer'
        ordering = ['-added_at']