from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from .models import Category, Post


# Display Blogs
class BlogTemplateView(TemplateView):
    template_name = 'blog/blog.html'


# Single Blog Details
class BlogDetailTemplateView(TemplateView):
    template_name = 'blog/blog_detail.html'

    def get_context_data(self, **kwargs):
        id = self.kwargs.get('pk')
        post = Post.objects.get(id=id)
        context = {'post': post}
        return context


# Add Blogs
class BlogAddTemplateView(TemplateView):
    template_name = 'blog/add_blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        context = {'categories': categories}
        return context


class BlogEditTemplateView(TemplateView):
    template_name = 'blog/edit_blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        id = self.kwargs.get('pk')
        post = Post.objects.get(id=id)
        context = {'categories': categories, 'post': post}
        return context
