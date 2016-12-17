from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from models import Post
from .forms import BlogPostForm
from django.contrib.auth.decorators import login_required


def post_list(request):
    return render(request, "blog_posts.html",
                  {'posts': Post.objects.filter(created_on__lte=timezone.now()).order_by('-created_on')})


@login_required(login_url='/login/')
def post_details(request, id):
    post = get_object_or_404(Post, pk=id)
    post.views += 1
    post.save()
    return render(request, "post_detail.html", {'post': post})


@login_required(login_url='/login/')
def new_post(request):
        if request.method == "POST":
            form = BlogPostForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return redirect(post_details, post.pk)
        else:
            return render(request, 'blog_post_form.html', {'form': BlogPostForm()})


@login_required(login_url='/login/')
def edit_post(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect(post_details, post.pk)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blog_post_form.html', {"form": form})
