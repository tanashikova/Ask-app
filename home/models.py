from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from tinymce.models import HTMLField


class Question (models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.CharField(max_length=150)
    date_posted = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ("-date_posted",)

    def __str__(self):
        return self.question

    def get_absolute_url(self):
            return reverse("question-detail", kwargs={"pk": self.pk})
          
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    email = models.EmailField(blank=True)
    date_submitted = models.DateTimeField(auto_now_add=True)
    answer_text = HTMLField()

    def __str__(self):
        return self.answer_text