from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect, Http404
from .models import Post
from .forms import PostForm
from django.contrib import messages


def post_index(request):
    posts = Post.objects.all()
    return render(request, "post/index.html", {'posts': posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
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

    if not request.user.is_authenticated():
        # Eğer kullanıcı giriş yapmamış ise hata sayfası gönder
        return Http404()

    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.save()
        messages.success(request, "Başarılı bir şekilde oluşturdunuz.", extra_tags='mesaj-basarili')
        return HttpResponseRedirect(post.get_absolute_url())

    context = {
        'form': form
    }

    return render(request, "post/form.html", context)


def post_update(request, slug):

    if not request.user.is_authenticated():
        # Eğer kullanıcı giriş yapmamış ise hata sayfası gönder
        return Http404()

    post = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        form.save()
        messages.success(request, "Başarılı bir şekilde güncellediniz.")
        return HttpResponseRedirect(post.get_absolute_url())

    context = {
        'form': form
    }

    return render(request, "post/form.html", context)


def post_delete(request, slug):

    if not request.user.is_authenticated():
        # Eğer kullanıcı giriş yapmamış ise hata sayfası gönder
        return Http404()

    post = get_object_or_404(Post, slug=slug)
    post.delete()
    return redirect("post:index")