from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Test')


def post_list(request):
    return render(request, 'post_list.html', {})


def test_html(request):
    return render(request, 'test_html.html', {})


def new(request):
    return HttpResponse('new')


def urltest(request):
    return HttpResponse('urltest text')
