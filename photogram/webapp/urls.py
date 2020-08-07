
from .views import hello, post_photo
from django.urls import path

urlpatterns = [
    path('hello/', hello),
    path('', post_photo)
]