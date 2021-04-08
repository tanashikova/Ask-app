from django.urls import path
from . import views
from .views import QuestionListView, QuestionDetailView, QuestionCreateView,  QuestionUpdateView, QuestionDeleteView, AddAnswerView, AnswerDeleteView


urlpatterns = [
     path('', QuestionListView.as_view(), name='home'),
     path('question/<int:pk>/', QuestionDetailView.as_view(), name='question-detail'),
     path('question/new/', QuestionCreateView.as_view(), name='question-create'),
     path('question/<int:pk>/update/', QuestionUpdateView.as_view(), name='question-update'),
     path('question/<int:pk>/delete/', QuestionDeleteView.as_view(), name='question-delete'),
     path('question/<int:pk>/answer', AddAnswerView.as_view(), name='answer-create'),
     path('question/<int:question_id>/edit_answer/<int:answer_id>/edit/', views.edit_answer, name="edit"),
     path('delete-answer/<int:pk>', AnswerDeleteView.as_view(), name='answer-delete'),
     path('about/', views.about, name='about'),
]