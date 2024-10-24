from django.shortcuts import render
from posts.models import Post
from django.http import HttpResponse
from posts.forms import PostForm, PostForm2
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from users.forms import SearchForm
from django.db.models import Q


@login_required(login_url='/register/')
def post_list_view(request):
    limit = 3
    if request.method == "GET":
        search = request.GET.get('search', None)
        tag = request.GET.getlist('tag', None)
        # ordering = request.GET.get('ordering', None)
        page = request.GET.get('page', 1)

        posts = Post.objects.all()

        if search:
            posts = posts.filter(
                Q(title__icontains=search) | Q(content__icontains=search))

        if tag:
            posts = posts.filter(tags__id__in=tag)

        # if ordering:
        #     print(ordering)
        #     posts = posts.order_by(ordering)

        max_pages = posts.count() / limit
        if round(max_pages) < max_pages:
            max_pages = round(max_pages) + 1
        else:
            max_pages = round(max_pages)

        start = (int(page)-1) * limit
        end = start * limit
        posts = posts[start:end]

        form = SearchForm
        return render(request, 'post_list.html', {
            'posts': posts,
            'form': form,
            'max_pages': range(1, max_pages + 1)})


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

