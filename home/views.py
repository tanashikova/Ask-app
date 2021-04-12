from django.shortcuts import render,redirect, get_object_or_404
from .models import Question,Answer
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import AnswerForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

def home(request):
    questions = Question.objects.all()
    return render(request, 'home/home.html', {'questions':questions})

def about(request):
    return render(request, 'home/about.html')

class QuestionListView(ListView):
    model = Question
    template_name = 'home/home.html'
    context_object_name = 'questions'


def LikeView(request, pk):
    question=get_object_or_404(Question, id=request.POST.get('question_id'))
    liked = False
    if question.likes.filter(id=request.user.id).exists():
        question.likes.remove(request.user)
        liked = False
    else:
        question.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('question-detail', args=[str(pk)]))

class QuestionDetailView(DetailView):
    model = Question
    template_name = 'home/question_detail.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super(QuestionDetailView, self).get_context_data(*args, **kwargs)
        data = get_object_or_404(Question, id=self.kwargs['pk'])
        likes_count = data.likes_count()
        liked = False
        if data.likes.filter(id=self.request.user.id).exists():
            liked = True

        context['likes_count'] = likes_count
        return context
   
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
        form.instance.user = self.request.user
        return super().form_valid(form)

    
    def get_success_url(self):

       return reverse_lazy('question-detail', kwargs={'pk': self.kwargs['pk']})

# edit answer function 
def edit_answer(request, question_id, answer_id):
  question = Question.objects.get(id=question_id)
  answer = Answer.objects.get(id=answer_id)
  edit_form = AnswerForm(request.POST or None, instance=answer)
  if request.POST and edit_form.is_valid():
    edit_form.save()
    return redirect('question-detail', question_id )

  else:
    return render(request,'home/edit.html', {'edit_form': edit_form, 'question':question, 'answer':answer })



class AnswerDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Answer
    success_url = '/'

    def test_func(self):
      answer = self.get_object()
      if self.request.user == answer.user:
        return True
      return False