# Backend

### intro
1. create the environment
   <code>python3 -m venv Py3Env </code>
2. activate the Environment
   <code>source Py3Env/bin/activate </code>
3. Install django
   <code>pip install django </code>

### create the project folder
1. <code>django-admin startproject (project_name) </code>
2. change directory into the project folder
3. run server <code>python3 manage.py runserver </code>


### create the apps folder
* cd apps
* in the terminal: <code> python3 ../manage.py startapp (app_name) </code>
* go to project folder settings.py
* add apps to "INSTALLED APPS" and add <code>'apps.app_name', </code>
* within the app folders go to app.py file and change name to <code> name = 'apps.(app_name)' </code>
* change directory back to the project folder <code> proj -> Python3 manage.py migrate </code>
* change the paths in the project folder 
```py
from django.urls import path, include           # import include
# from django.contrib import admin              # comment out, or just delete
urlpatterns = [
    path('', include('your_app_name_here.urls')),	   
    # path('admin/', admin.sites.urls)         # comment out, or just delete
]
```
* add your "urls.py" into your apps
```py
from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),	   
]
```

* add this to views.py  into our apps
```py
from django.shortcuts import render, HttpResponse
def index(request):
    return HttpResponse("this is the equivalent of @app.route('/')!")
```