from django.http import HttpRequest
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.

# Class based View
def item(request):
    return HttpResponse("welcome to product page")

class MyView(View):
    def get(Self, request):
        return HttpResponse("this is class based view")