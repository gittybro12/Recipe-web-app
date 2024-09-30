from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import PostCreate

# Create your views here.

class postViews(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'

    def get_queryset(self): 
        return Post.objects.order_by('-date_created')

class detailed_view(LoginRequiredMixin,DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

class create_view(LoginRequiredMixin,CreateView):
    model = Post
    form_class = PostCreate
    template_name = 'post_create.html'
    success_url = reverse_lazy('Home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class update_view(LoginRequiredMixin,UpdateView):
    model = Post
    form_class = PostCreate
    template_name = 'post_create.html'
    success_url = reverse_lazy('Home')


class delete_view(LoginRequiredMixin,DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy('Home')



def search(request):
    if request.method == 'POST':
        searched = request.POST.get('searched', '')
        recipes = Post.objects.filter(title__contains=searched)
        return render(request, 'search_result.html', {'searched':searched, 'recipes':recipes} )
    else:
        searched = None
        return render(request, 'search_result.html', {'searched':searched} )







