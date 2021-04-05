from django.shortcuts import render
from .models import Question


def home(request):
    questions = Question.objects.all()
    return render(request, 'home/home.html', {'questions':questions})

def about(request):
    return render(request, 'home/about.html')