from django.contrib import admin
from django.urls import path
from .views import users, create_user, user

urlpatterns = [
    path('', users, name="users"),
    path('<int:user_id>/', user, name="user"),
    path('create/', create_user, name="create_user"),
]
