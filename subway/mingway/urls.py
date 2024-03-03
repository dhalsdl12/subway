from django.urls import path
from .views import MingSubwayToWork, MingSubwayToHouse
from .views import WorkKonkuk, WorkJamsil, WorkSadang
from .views import HomeMunjung, HomeJamsilToKonkuk, HomeJamsilToSadang

urlpatterns = [
    path('subway/work', MingSubwayToWork.as_view(), name='subwayToWork'),
    path('subway/house', MingSubwayToHouse.as_view(), name='subwayToHouse'),
    path('subway/work/konkuk', WorkKonkuk.as_view(), name='work-konkuk'),
    path('subway/work/jamsil', WorkJamsil.as_view(), name='work-jamsil'),
    path('subway/work/sadang', WorkSadang.as_view(), name='work-sadang'),
    path('subway/home/munjung', HomeMunjung.as_view(), name='home-munjung'),
    path('subway/home/jamsil-konkuk', HomeJamsilToKonkuk.as_view(), name='home-jamsil-konkuk'),
    path('subway/home/jamsil-sadang', HomeJamsilToSadang.as_view(), name='home-jamsil-sadang'),
]