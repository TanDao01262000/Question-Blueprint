from django.urls import path
from . import views
from.views import upvote
app_name = 'question_blueprint'

urlpatterns = [
    path('', views.home, name='home'),
    path('question/', views.QuestionListView.as_view(), name='question_view'),
    path('question/<int:pk>/', views.QuestionDetailView.as_view(), name='question_detail_view'),
    path('question/<int:pk>/update', views.QuestionUpdateView.as_view(), name='question_update_view'),
    path('question/<int:pk>/delete', views.QuestionDeleteView.as_view(), name='question_delete_view'),
    path('question/ask/', views.QuestionCreateView.as_view(), name='question_ask_view'),

    # answer
    path('question/<int:pk>/answer/', views.AnswerAddView.as_view(), name='answer'),
    path('question/<int:pk>/upvote/', views.upvote, name='upvote'),

]