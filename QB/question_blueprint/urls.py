from django.urls import path
from . import views

app_name = 'question_blueprint'

urlpatterns = [
    path('', views.home, name='home'),
    path('question/', views.QuestionListView.as_view(), name='question_view'),
]