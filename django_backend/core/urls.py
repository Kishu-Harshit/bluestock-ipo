from django.urls import path
from .views import hello, frontend_view, call_node_backend, from_node

urlpatterns = [
    path('hello/', hello),
    path('', frontend_view),
    path('call-node/', call_node_backend),
    path('api/from-node/', from_node),
]
