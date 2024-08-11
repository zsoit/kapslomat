from django.urls import path
from . import views

urlpatterns = [
    path('decode/', views.decode_view, name='decode_view'),
]
