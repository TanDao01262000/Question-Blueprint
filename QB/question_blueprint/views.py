from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView,  CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Question, Answer, Upvote
from .forms import AnswerForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import HttpResponseBadRequest
# Create your views here.

def home(request):
    # if request.method == 'POST':
    return render(request, 'home.html')

# Fully CRUD functionality for the app
class QuestionListView(ListView):
    model = Question
    context_object_name = 'questions'
    ordering = ["-created_date"]


class QuestionDetailView(LoginRequiredMixin, DetailView):
    model = Question
    context_object_name = 'single_question'



class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    context_object_name = 'single_question'
    fields = ['title', 'content', 'tag']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class QuestionUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView, ):
    model = Question
    fields = ['title', 'content', 'tag']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    # prevent people change others' questions
    def test_func(self):
        ques = self.get_object()
        if self.request.user == ques.user:
            return True
        return False
    

class QuestionDeleteView( UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Question
    context_object_name = 'single_question'
    success_url = '/question/'
    
    def test_func(self):
        ques = self.get_object()
        if self.request.user == ques.user:
            return True
        return False


class AnswerDetailView(CreateView):
    model = Answer
    context_object_name = 'ans'
    form_clas = AnswerForm
    template_name = 'question_blueprint/question_detail.html'
    success_url = reverse_lazy('question_blueprint:question_view')
    

    def form_valid(self, form):
        form.instance.question_id = self.kwargs['pk']
        return super().form_valid(form)
    
    def get_queryset(self):
        return Answer.objects.order_by('-created_date')
    


    

class AnswerAddView(CreateView):

    model = Answer
    ordering = ["-created_date"]
    context_object_name = 'single_question'
    form_class = AnswerForm
    template_name = 'question_blueprint/answer.html'
    
    def get_queryset(self):
        return Answer.objects.order_by('-created_date')

    def form_valid(self, form):
        self.success_url = reverse_lazy('question_blueprint:question_detail_view', args=[self.kwargs['pk']])
        form.instance.question_id = self.kwargs['pk']
        form.instance.user_id = self.request.user.id
        # add toxicity test here
        return super().form_valid(form)
    

@login_required
def upvote(request, pk):
    answer = get_object_or_404(Answer, id=pk)

    if request.method == "POST":
        upvote = Upvote.objects.filter(answer=answer, user=request.user).first()

        if upvote:
            upvote.delete()
        else:
            Upvote.objects.create(answer=answer, user=request.user)
            print(f"KKKKKKKK: {request.POST.get('pk')}")
    
    return redirect('question_blueprint:question_detail_view', request.POST.get('pk'))
    
    # checking whether current user has ever upvoted the answer or not
    