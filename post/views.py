from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect
from .models import Post
from .forms import PostForm


def post_index(request):
    posts = Post.objects.all()
    return render(request, "post/index.html", {'posts': posts})


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    context = {
        'post': post
    }
    return render(request, "post/detail.html", context)


def post_create(request):
    # if request.method == "POST":
    #     print(request.POST)
    #
    # title = request.POST.get("title")
    # content = request.POST.get("metin")
    # Post.objects.create(title=title, content=content)

    # if request.method == "POST":
    #     # Formdan gelen bilgileri kaydet
    #     form = PostForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    # else:
    #     # Formu kullanıcıya göster
    #     form = PostForm()

    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save()
        return HttpResponseRedirect(post.get_absolute_url())

    context = {
        'form': form
    }

    return render(request, "post/form.html", context)


def post_update(request, id):
    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(post.get_absolute_url())
    
    context = {
        'form': form
    }

    return render(request, "post/form.html", context)


def post_delete(request):
    return HttpResponse("Burası Post silme sayfası")