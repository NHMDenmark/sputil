from django.http import HttpResponse
from django.shortcuts import redirect

def index(request):
  return HttpResponse('<a href="/admin/">Admin</a><br/><a href="/spwift/">SpWIFT</a>')

def redirect_view(request):
    response = redirect('/spwift/')
    return response