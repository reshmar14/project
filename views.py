from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def new(request):
    return HttpResponse("HOME")
def about(request):
    return render(request,"about.html")
def contact(request):
    return HttpResponse("contact")
def detail(request):
    return render(request,"detail.html")
def thanks(request):
    return HttpResponse("thanks")