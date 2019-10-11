from django.http import JsonResponse
import requests


def index(request):
    result = requests.get("https://api.spacexdata.com/v3/launches")
    return JsonResponse(result.json(), content_type="application/json")