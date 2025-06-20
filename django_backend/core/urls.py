from django.urls import path
from .views import hello, frontend_view

urlpatterns = [
    path('hello/', hello),
    path('', frontend_view),
]
