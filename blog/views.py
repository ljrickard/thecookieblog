from django.shortcuts import render
from django.utils import timezone
from models import Post


def post_list(request):
    return render(request, "blog_posts.html",
                  {'posts': Post.objects.filter(published_on__lte=timezone.now()).order_by('-published_on')})
