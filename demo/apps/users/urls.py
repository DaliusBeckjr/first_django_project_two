from django.urls import path
from . import views	# the . indicates that the views file can be found in the same directory as this file

urlpatterns = [
    path('', views.index, name="index"),
    path('register', views.register, name="reg"),
    path('login', views.login, name="login"),
    path('users/new', views.create_user, name="create_user"),
    path('users', views.display, name="display_user")
]
