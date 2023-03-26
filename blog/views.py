from django.http import HttpResponse
from django.shortcuts import render
from .models import Question


# Create your views here.
def index(request):
    return render(request, "index.html")

def blogs(request):
    return HttpResponse("blogs")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def signup(request):
    return render(request, "signup.html")

def blog_details(request, id):
    return HttpResponse("blog details: " + str(id))

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)