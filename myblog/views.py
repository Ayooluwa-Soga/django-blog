from django.shortcuts import render
from django.views import generic
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class PostList(generic.ListView):
    # queryset = Post.objects.filter(status=1).order_by('-created_on')
    queryset = Post.objects.all().order_by('title')
    paginate_by = 2
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

