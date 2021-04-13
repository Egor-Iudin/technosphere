from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def message(request, message_id):
    if request.method == 'GET':
        return JsonResponse({
            'status': 'ok',
            'message_id': message_id,
            'data':
            [
                'test',
                'users',
                'media_urls'
            ],
        })


# @csrf_exempt
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
