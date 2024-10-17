from django.shortcuts import render
from posts.models import Post
from django.http import HttpResponse
from posts.forms import PostForm


def post_list_view(request):
    if request.method == "GET":
        posts = Post.objects.all()
        return render(request, 'post_list.html', {'posts': posts})


def based(request):
    if request.method == "GET":
        return render(request, 'base.html')


def post_detail(request, post_id):
    if request.method == "GET":
        post = Post.objects.get(id=post_id)
        return render(request, 'post_detail.html', {'post': post})


def post_create(request):
    if request.method == "GET":
        return render(request, 'post_create.html')
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        post = Post.objects.create(title=title, content=content, image=image)
        return HttpResponse(f'post with name {post.title} has been created!')

