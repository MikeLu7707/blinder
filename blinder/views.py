from datetime import datetime
import imp
from multiprocessing import context
from pipes import Template
from typing import Generic
from urllib import request
from django import template
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from multiprocessing import context
from pydoc import render_doc
from webbrowser import get
from gc import get_objects

from django.views import View
from django.views.generic import TemplateView
from .models import Book, Post, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CommentForm




# Create your views here.
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {"knowledge": books}) 


def displayTime(request):
    now = datetime.now()
    html = "Time is{}  ".format(now)
    return HttpResponse(html)

def displayContact(request):
    return HttpResponse("Welcome")

def post_list(request):
    post_list=Post.objects.all()
    paginator= Paginator(post_list, 5)
    page=request.GET.get('page')
    try:
        posts=paginator.page(page)
    except PageNotAnInteger:
        posts=paginator.page(1)
    except EmptyPage:
        posts=paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'page':page,"posts": posts})

##Views for all post
def post(request):
    posts = Post.objects.all()
    return render()

##Single post
def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published', publish__year= year, publish__month=month, publish__day=day)
    comments=post.comments.filter(active=True)
    new_comment=None 
    if request.method=='POST':
        comment_form=CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment=comment_form.save(commit=False)
            new_comment.post=post
            new_comment.save()
    else:
        comment_form=CommentForm()
    return render(request,'post_detail.html', {'post':post,'comments':comments,'new_comment':new_comment,'comment_form':comment_form})
    


# Class based View
class MyView(TemplateView):
    template_name = 'index.html'
    def get(Self, **kwargs):
        context = super().get(**kwargs)
        template_name = 'index.html'
        context = {
            "page": template_name 
        } 
        return context



