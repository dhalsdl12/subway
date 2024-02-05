from django.urls import path
from .views import MingSubwayToWork, MingSubwayToHouse

urlpatterns = [
    path('subway/work', MingSubwayToWork.as_view(), name='subwayToWork'),
    path('subway/house', MingSubwayToHouse.as_view(), name='subwayToHouse'),
]