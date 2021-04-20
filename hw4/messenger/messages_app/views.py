from django.http import JsonResponse
from django.shortcuts import render

from django.contrib.auth.models import User
from .models import Message


def message(request, user_id):
    if request.method == 'GET':
        data = [[i.text, i.created_date, [[i.username, i.id] for i in list(
            i.users.all())]] for i in Message.objects.filter(users=User.objects.get(id=user_id))]
        return JsonResponse({
            'status': 'ok',
            'user_id': user_id,
            'data': data,
        })


def create_message(request):
    if request.method == 'POST':
        return JsonResponse({
            'status': 'ok',
            'message_id': 4,
            'data':
            [
                'test',
                'users',
                'media_urls'
            ],
        })
    if request.method == 'GET':
        return render(request, template_name='create.html')
