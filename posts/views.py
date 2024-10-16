from django.shortcuts import render
from posts.models import Post


def post_list_view(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})


def based(request):
    return render(request, 'base.html')


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'post_detail.html', {'post': post})
