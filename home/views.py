from django.shortcuts import render
from .models import Question,Answer
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import AnswerForm
from django.urls import reverse_lazy

def home(request):
    questions = Question.objects.all()
    return render(request, 'home/home.html', {'questions':questions})

def about(request):
    return render(request, 'home/about.html')

class QuestionListView(ListView):
    model = Question
    template_name = 'home/home.html'
    context_object_name = 'questions'

class QuestionDetailView(DetailView):
    model = Question

   


class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    fields = ['question']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        question = self.get_object()
        if self.request.user == question.author:
            return True
        return False
class QuestionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Question
    fields = ['question']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        question = self.get_object()
        if self.request.user == question.author:
            return True
        return False
class QuestionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Question
    success_url = '/'

    def test_func(self):
        question = self.get_object()
        if self.request.user == question.author:
            return True
        return False



class AddAnswerView(LoginRequiredMixin, CreateView):
    model = Answer
    form_class = AnswerForm
    template_name = 'home/add_answer.html'

    def form_valid(self, form):
        form.instance.question_id = self.kwargs['pk']
        return super().form_valid(form)

    
    def get_success_url(self):

       return reverse_lazy('question-detail', kwargs={'pk': self.kwargs['pk']})
    #  def test_func(self):
    #     question = self.get_object()
    #     if self.request.user == question.author:
    #         return True
    #     return False