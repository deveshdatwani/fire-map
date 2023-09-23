from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "map.html")


def hello(reques):
    return HttpResponse("Hello world!")


def question(request, question_id):
    return HttpResponse(f'The question id is {question_id}')