from django.urls import path
from .views import MingSubway

urlpatterns = [
    path('subway/', MingSubway.as_view(), name='subway'),
]