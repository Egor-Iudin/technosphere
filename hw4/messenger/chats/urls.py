from django.contrib import admin
from django.urls import path
from .views import chats, create_chat, chat

urlpatterns = [
    path('', chats, name="chats"),
    path('<int:chat_id>/', chat, name="chat"),
    path('create/', create_chat, name="create_chat"),
]
