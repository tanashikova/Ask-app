from django.shortcuts import render
from .models import Question, Answer
from django.forms import ModelForm, HiddenInput
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
# from captcha.fields import CaptchaField

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

    def get_context_data(self, **kwargs):
        context = super(QuestionDetailView, self).get_context_data(**kwargs)
        answer_form = AnswerCreateForm()
        context['answer_form'] = answer_form
        return context

class AnswerCreateForm(ModelForm):

    # captcha = CaptchaField()

    class Meta:
        model = Answer
        fields = "__all__"
        widgets = {'question': HiddenInput()}
        
class AnswerCreate(CreateView):
    model = Answer
    form_class = AnswerCreateForm

    def get_success_url(self):
        return reverse('home:question-detail', kwargs={'pk': self.object.question.pk})
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



