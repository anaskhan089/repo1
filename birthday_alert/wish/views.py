from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def wish_view(request):
    s='<h1> Northern Motorsports Wishes you a very happy Birthday </h1>'
    return HttpResponse(s)
