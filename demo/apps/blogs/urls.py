from django.urls import path     
from . import views

app_name = "blogs"

urlpatterns = [
    path('', views.index, name= "index"), # /blogs/
    path('new', views.new_blog, name= "new"), # /blogs/new
    path('create', views.create_blog, name= "create"), #/blogs/create
    path('<number>', views.show, name= "show"), #/blogs/show
    path('<number>/edit', views.edit, name = 'edit'), 
    path('<number>/delete', views.delete, name = 'delete'),
]
