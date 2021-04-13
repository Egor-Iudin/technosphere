from django.contrib import admin
from django.urls import path
from .views import message, create_message

urlpatterns = [
    path('<int:message_id>/', message, name="message"),
    path('create/', create_message, name="create_message"),
]
