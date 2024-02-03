from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import os, json, logging, requests
from pathlib import Path
from django.core.exceptions import ImproperlyConfigured

class MingSubway(APIView):
    def get(self, request, format=None):

        BASE_DIR = Path(__file__).resolve().parent.parent
        secret_file = os.path.join(BASE_DIR, 'secret.json')

        with open(secret_file) as f:
            secrets = json.loads(f.read())

        def get_secret(setting):
            try:
                return secrets[setting]
            except KeyError:
                error_msg = 'key error'
                raise ImproperlyConfigured(error_msg)

        base_url = "http://swopenapi.seoul.go.kr/api/subway/"
        subway_key = get_secret('SUBWAY_KEY')
        url = base_url + subway_key + "/json/realtimeStationArrival/0/5/"
        
        response = requests.get(url + "성수")

        if response.status_code == 200:
            data = response.json()
            print(data)
        else:
            print("Error:", response.status_code)
            
        return Response("Ming's Subway", status=status.HTTP_200_OK)