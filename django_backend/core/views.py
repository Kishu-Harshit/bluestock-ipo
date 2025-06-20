from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

import os
from django.http import HttpResponse
from django.conf import settings

def frontend_view(request):
    index_path = os.path.join(settings.BASE_DIR, '..', 'frontend', 'index.html')
    index_path = os.path.abspath(index_path)
    with open(index_path, 'r', encoding='utf-8') as f:
        return HttpResponse(f.read())


@api_view(['GET'])
def hello(request):
    return Response({"message": "Hello from Django API"})
