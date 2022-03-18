from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>SpWIFT</h1><h3>Specify Web-based Import Facilitation Tool</h3><p>(under construction...)</p>")
