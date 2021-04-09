from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse



class Question (models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.CharField(max_length=150)
    date_posted = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, related_name='question_likes')

    class Meta:
        ordering = ("-date_posted",)

    def __str__(self):
        return self.question

    def likes_count(self):
        return self.likes.count()

    def get_absolute_url(self):
            return reverse("question-detail", kwargs={"pk": self.pk})


class Answer (models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_submited = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_submited',)


    def __str__(self):
        return self.content
