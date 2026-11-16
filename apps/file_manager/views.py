from django.http import JsonResponse

def upload_attachment(request):
    return JsonResponse({'module': 'file_manager', 'supported_formats': ['pdf', 'png', 'jpg']})
