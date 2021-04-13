from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def users(request):
    if request.method == 'GET':
        return JsonResponse({
            'status': 'ok',
            'users': [
                {
                    'user_id': 1,
                    'data':
                    [
                        'name',
                        'surname',
                    ],
                },
                {
                    'user_id': 2,
                    'data':
                    [
                        'name',
                        'surname',
                    ],
                },
                {
                    'user_id': 3,
                    'data':
                    [
                        'name',
                        'surname',
                    ],
                },
            ],
        })


def user(request, user_id):
    if request.method == 'GET':
        return JsonResponse({
            'status': 'ok',
            'user_id': user_id,
            'data':
            [
                'name',
                'surname',
            ],
        })


# @csrf_exempt
def create_user(request):
    if request.method == 'POST':
        return JsonResponse({
            'status': 'ok',
            'user_id': 4,
            'data':
            [
                'name',
                'surname',
            ],
        })
    if request.method == 'GET':
        return render(request, template_name='create.html')
