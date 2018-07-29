from __future__ import unicode_literals
from django.shortcuts import render
from django.http import  HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import  Post

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

#class IndexView(generic.ListView):
 #   template_name = 'blog/post_list.html'
  #  context_object_name = 'latest_post_list'
    
   # def get_queryset(self):
    #   return Post.objects.order_by('-pub_date')[:5]
