from django.urls import path, include
from . import views
from .views import QuestionListView, QuestionDetailView, QuestionCreateView,  QuestionUpdateView, QuestionDeleteView, AnswerCreate

urlpatterns = [
     path('tinymce/', include('tinymce.urls')),
     path('', QuestionListView.as_view(), name='home'),
     path('question/<int:pk>/', QuestionDetailView.as_view(), name='question-detail'),
     path('answer', AnswerCreate.as_view(), name='answer_form'),
     path('question/new/', QuestionCreateView.as_view(), name='question-create'),
     path('question/<int:pk>/update/', QuestionUpdateView.as_view(), name='question-update'),
     path('question/<int:pk>/delete/', QuestionDeleteView.as_view(), name='question-delete'),
     path('about/', views.about, name='about'),
]