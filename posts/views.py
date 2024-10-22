from django.shortcuts import render
from posts.models import Post
from django.http import HttpResponse
from posts.forms import PostForm, PostForm2
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


@login_required(login_url='/register/')
def post_list_view(request):
    if request.method == "GET":
        posts = Post.objects.all()
        return render(request, 'post_list.html', {'posts': posts})


@login_required(login_url='/register/')
def based(request):
    if request.method == "GET":
        return render(request, 'base.html')


@login_required(login_url='/register/')
def post_detail(request, post_id):
    if request.method == "GET":
        post = Post.objects.get(id=post_id)
        return render(request, 'post_detail.html', {'post': post})


@login_required(login_url='/register/')
def post_create(request):
    if request.method == "GET":
        form = PostForm2()
        return render(request, 'post_create.html', context={'form': form})
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, 'post_create.html', context={'form': form})
        title = form.cleaned_data['title']
        content = form.cleaned_data.get('content')
        image = form.cleaned_data['image']
        post = Post.objects.create(title=title, content=content, image=image)
        return redirect('/posts/')

