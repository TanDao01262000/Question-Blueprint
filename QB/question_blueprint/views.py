from django.shortcuts import render
from django.views.generic import ListView, DetailView,  CreateView, DeleteView, UpdateView
from .models import Question
# Create your views here.

def home(request):
    # if request.method == 'POST':
    return render(request, 'home.html')

# Fully CRUD functionality for the app
class QuestionListView(ListView):
    model = Question
    context_object_name = 'questions'
    ordering = ["-created_date"]


class QuestionDetailView(DetailView):
    model = Question
    context_object_name = 'single_question'
