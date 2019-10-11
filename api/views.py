from django.http import JsonResponse


def index(request):
    return JsonResponse({'foo':'bar'}, content_type="application/json")