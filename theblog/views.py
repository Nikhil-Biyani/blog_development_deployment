from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy


# Create your views here.
def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-posted_date']


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'


class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    # fields = ['title', 'title_tag', 'body']


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
