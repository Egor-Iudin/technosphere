from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def chats(request):
    if request.method == 'GET':
        return JsonResponse({
            'status': 'ok',
            'chats': [
                {
                    'chat_id': 1,
                    'data':
                    [
                        'test',
                        'users',
                        'media_urls'
                    ],
                },
                {
                    'chat_id': 2,
                    'data':
                    [
                        'test',
                        'users',
                        'media_urls'
                    ],
                },
                {
                    'chat_id': 3,
                    'data':
                    [
                        'test',
                        'users',
                        'media_urls'
                    ],
                },
            ],
        })
    if request.method == 'POST':
        return JsonResponse({
            'status': 'not ok'
        })


def chat(request, chat_id):
    if request.method == 'GET':
        return JsonResponse({
            'status': 'ok',
            'chat_id': chat_id,
            'data':
            [
                'test',
                'users',
                'media_urls'
            ],
        })
    if request.method == 'POST':
        return JsonResponse({
            'status': 'not ok'
        })


# @csrf_exempt
def create_chat(request):
    if request.method == 'POST':
        return JsonResponse({
            'status': 'ok',
            'chat_id': 4,
            'data':
            [
                'test',
                'users',
                'media_urls'
            ],
        })
    if request.method == 'GET':
        return render(request, template_name='create.html')
