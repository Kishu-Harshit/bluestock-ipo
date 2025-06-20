from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
import os
import json
from django.http import HttpResponse, JsonResponse
from django.conf import settings

def frontend_view(request):
    index_path = os.path.join(settings.BASE_DIR, '..', 'frontend', 'index.html')
    index_path = os.path.abspath(index_path)
    with open(index_path, 'r', encoding='utf-8') as f:
        return HttpResponse(f.read())

def call_node_backend(request):
    data_to_send = {'name': 'Django', 'message': 'Hello from Django!'}
    try:
        response = requests.post('http://localhost:3001/api/from-django', json=data_to_send)
        return JsonResponse({'node_response': response.json()})
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)

@api_view(['GET'])
def hello(request):
    return Response({"message": "Hello from Django API"})

@csrf_exempt
def from_node(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print("Received from Node.js:", data)
            return JsonResponse({'status': 'success', 'message': 'Django received data from Node.js', 'data': data})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid method'}, status=405)