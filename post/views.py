from django.shortcuts import render, HttpResponse


def post_index(request):
    return HttpResponse("Burası Post index sayfası")


def post_detail(request):
    return HttpResponse("Burası Post detay sayfası")


def post_create(request):
    return HttpResponse("Burası Post oluşturma sayfası")


def post_update(request):
    return HttpResponse("Burası Post güncelleme sayfası")


def post_delete(request):
    return HttpResponse("Burası Post silme sayfası")