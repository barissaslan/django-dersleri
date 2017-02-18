from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Post


def post_index(request):
    posts = Post.objects.all()
    return render(request, "post/index.html", {'posts': posts})


def post_detail(request):
    post = get_object_or_404(Post, id=2)
    context = {
        'post': post
    }
    return render(request, "post/detail.html", context)


def post_create(request):
    return HttpResponse("Burası Post oluşturma sayfası")


def post_update(request):
    return HttpResponse("Burası Post güncelleme sayfası")


def post_delete(request):
    return HttpResponse("Burası Post silme sayfası")