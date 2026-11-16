from django.http import JsonResponse

def login_view(request):
    return JsonResponse({'module': 'authentication', 'status': 'active', 'reusable': True})

def logout_view(request):
    return JsonResponse({'module': 'authentication', 'action': 'logout'})
