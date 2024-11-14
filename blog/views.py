from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import View
from .models import BlogPost, Comments
from blog.forms import CommentForm


# Create your views here.
def blog_home(request):
    posts = BlogPost.objects.all().order_by("-pub_date")
    context = {
        "posts": posts,
    }
    return render(request, 'blog/home.html', context)



def blog_category(request, category):
    posts = BlogPost.objects.filter(
        categories__name__contains=category).order_by("-pub_date")
    context = {
        'category': category,
        'posts': posts
        
        }
    return render(request, 'blog/category.html', context)
    



def blog_detail(request, id):
    
    post = BlogPost.objects.get(id=id)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comments(
                author=form.cleaned_data['author'],
                body=form.cleaned_data['body'],
                post=post,
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)
            
    comments = Comments.objects.filter(post=post)
    context = {
        'post': post,
        'comments': comments,
        'form': CommentForm(),
 }
    return render(request, 'blog/post.html', context)



def about_me(request):
    return render(request, 'blog/about.html')





