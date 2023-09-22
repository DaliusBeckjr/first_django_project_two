from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("this is the equivalent of @app.route!")


def new_blog(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create_blog(request):
    return redirect("/blogs")

def show(request, number):
    return HttpResponse(f"placeholder to display blog number: {number}")

def edit(request, number):
    return HttpResponse(f"placeholder to edit blog {number}")

def delete(request, number):
    return redirect("/blogs")