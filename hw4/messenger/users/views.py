from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User


def users(request):
    if request.method == 'GET':
        users = [[i.username, i.id] for i in User.objects.all()]
        return JsonResponse({
            'status': 'ok',
            'users': users})


def user(request, user_id):
    if request.method == 'GET':
        if not User.objects.filter(id=user_id).exists():
            return JsonResponse({
            'status': 'not ok',
            'error': "user does not exist",
        })
        
        user = User.objects.get(id=user_id)
        data = [user.username, user.id]
        return JsonResponse({
            'status': 'ok',
            'user_id': user_id,
            'data': data,
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
