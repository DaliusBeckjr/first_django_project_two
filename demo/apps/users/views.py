from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    if request.method == "GET":
        return render(request, "index.html")

def register(request):
    return HttpResponse("placeholder for users to create a new user record")

def login(request):
    return HttpResponse("placeholder for users to log in")

def create_user(request):
    # have the same method that handles /register also handle the url request of /users/new
    print("Got Post Info..........")
    print(request.POST)
    return render(request, "index.html")

def display(request):
    return HttpResponse("placeholder to later display all the list of users")