
from .views import hello, index
from django.urls import path

urlpatterns = [
    path('hello/', hello),
    path('', index)
]