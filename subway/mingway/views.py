from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import os, json, logging, requests
from pathlib import Path
from django.core.exceptions import ImproperlyConfigured

class MingSubwayToWork(APIView):
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

        subway_infomation = ["Ming's Subway to house"]
        dic_eng = {
            "건대입구" : "Konkuk",
            "잠실" : "Jamsil",
            "문정" : "Munjeong",
            "사당" : "Sadang",
        }

        subwayStation = ['Konkuk','Jamsil','Sadang']

        for station in subwayStation:
            with open('./mingway/realtimeSubway/' + station + '.json', 'r', encoding='utf-8') as file:
                subway_info = json.load(file)

            if station == 'Konkuk':
                infomation = []
                for info in subway_info:
                    subwayId = info['subwayId']
                    trainLineNm = info['trainLineNm']

                    if subwayId[-1] == '2':
                        if '구의' in trainLineNm:
                            infomation.append({
                                'barvlDt' : info['barvlDt'],
                                'arvlMsg2' : info['arvlMsg2'],
                                'arvlMsg3' : info['arvlMsg3'],
                            })
                subway_infomation.append({'Konkuk Station' : infomation})
                    
            elif station == 'Jamsil':
                infomation = []
                
                for info in subway_info:
                    subwayId = info['subwayId']
                    trainLineNm = info['trainLineNm']
                    
                    if subwayId[-1] == '8':
                        if '석촌' in trainLineNm or '모란' in trainLineNm:
                            infomation.append({
                                'barvlDt' : info['barvlDt'],
                                'arvlMsg2' : info['arvlMsg2'],
                                'arvlMsg3' : info['arvlMsg3'],
                            })
                subway_infomation.append({'Jamsil Station' : infomation})
            elif station == 'Sadang':
                infomation = []
                
                for info in subway_info:
                    subwayId = info['subwayId']
                    trainLineNm = info['trainLineNm']
                    
                    if subwayId[-1] == '2':
                        if '방배' in trainLineNm:
                            infomation.append({
                                'barvlDt' : info['barvlDt'],
                                'arvlMsg2' : info['arvlMsg2'],
                                'arvlMsg3' : info['arvlMsg3'],
                            })
                subway_infomation.append({'Sadang Station' : infomation})
        print()
        return Response(subway_infomation, status=status.HTTP_200_OK)
    

class MingSubwayToHouse(APIView):
    def get(self, request, format=None):
        return Response("Ming's Subway to house", status=status.HTTP_200_OK)
    

class WorkKonkuk(APIView):
    def get(self, request, format=None):
        BASE_DIR = Path(__file__).resolve().parent.parent
        secret_file = os.path.join(BASE_DIR, 'secret.json')

        with open(secret_file) as f:
            secrets = json.loads(f.read())

        subway_infomation = ["Ming's Subway to work"]
        base_url = "http://swopenapi.seoul.go.kr/api/subway/"
        subway_key = secrets['SUBWAY_KEY']
        url = base_url + subway_key + "/json/realtimeStationArrival/0/10/건대입구"

        response = requests.get(url)
    
        if response.status_code == 200:
            infomation = []
            data = response.json()["realtimeArrivalList"]

            for info in data:
                subwayId = info['subwayId']
                trainLineNm = info['trainLineNm']

                if subwayId[-1] == '2':
                    if '구의' in trainLineNm:
                        infomation.append({
                            'barvlDt' : info['barvlDt'],
                            'arvlMsg2' : info['arvlMsg2'],
                            'arvlMsg3' : info['arvlMsg3'],
                        })
            subway_infomation.append({'Konkuk Station' : infomation})
            
            print(subway_infomation)
            return Response(subway_infomation, status=status.HTTP_200_OK)
        else:
            print("Error:", response.status_code)


class WorkJamsil(APIView):
    def get(self, request, format=None):
        BASE_DIR = Path(__file__).resolve().parent.parent
        secret_file = os.path.join(BASE_DIR, 'secret.json')

        with open(secret_file) as f:
            secrets = json.loads(f.read())

        subway_infomation = ["Ming's Subway to work"]
        base_url = "http://swopenapi.seoul.go.kr/api/subway/"
        subway_key = secrets['SUBWAY_KEY']
        url = base_url + subway_key + "/json/realtimeStationArrival/0/10/잠실"

        response = requests.get(url)
    
        if response.status_code == 200:
            infomation = []
            data = response.json()["realtimeArrivalList"]

            for info in data:
                subwayId = info['subwayId']
                trainLineNm = info['trainLineNm']

                if subwayId[-1] == '8':
                    if '석촌' in trainLineNm or '모란' in trainLineNm:
                        infomation.append({
                            'barvlDt' : info['barvlDt'],
                            'arvlMsg2' : info['arvlMsg2'],
                            'arvlMsg3' : info['arvlMsg3'],
                        })
            subway_infomation.append({'Jamsil Station' : infomation})
            
            print(subway_infomation)
            return Response(subway_infomation, status=status.HTTP_200_OK)
        else:
            print("Error:", response.status_code)


class WorkSadang(APIView):
    def get(self, request, format=None):
        BASE_DIR = Path(__file__).resolve().parent.parent
        secret_file = os.path.join(BASE_DIR, 'secret.json')

        with open(secret_file) as f:
            secrets = json.loads(f.read())

        subway_infomation = ["Ming's Subway to work"]
        base_url = "http://swopenapi.seoul.go.kr/api/subway/"
        subway_key = secrets['SUBWAY_KEY']
        url = base_url + subway_key + "/json/realtimeStationArrival/0/10/사당"

        response = requests.get(url)
    
        if response.status_code == 200:
            infomation = []
            data = response.json()["realtimeArrivalList"]

            for info in data:
                subwayId = info['subwayId']
                trainLineNm = info['trainLineNm']

                if subwayId[-1] == '2':
                    if '방배' in trainLineNm:
                        infomation.append({
                            'barvlDt' : info['barvlDt'],
                            'arvlMsg2' : info['arvlMsg2'],
                            'arvlMsg3' : info['arvlMsg3'],
                        })
            subway_infomation.append({'Sadang Station' : infomation})
            
            print(subway_infomation)
            return Response(subway_infomation, status=status.HTTP_200_OK)
        else:
            print("Error:", response.status_code)


class HomeMunjung(APIView):
    def get(self, request, format=None):
        BASE_DIR = Path(__file__).resolve().parent.parent
        secret_file = os.path.join(BASE_DIR, 'secret.json')

        with open(secret_file) as f:
            secrets = json.loads(f.read())

        subway_infomation = ["Ming's Subway to home"]
        base_url = "http://swopenapi.seoul.go.kr/api/subway/"
        subway_key = secrets['SUBWAY_KEY']
        url = base_url + subway_key + "/json/realtimeStationArrival/0/10/문정"

        response = requests.get(url)
    
        if response.status_code == 200:
            infomation = []
            data = response.json()["realtimeArrivalList"]

            for info in data:
                subwayId = info['subwayId']
                trainLineNm = info['trainLineNm']

                if subwayId[-1] == '8':
                    if '가락시장' in trainLineNm:
                        infomation.append({
                            'barvlDt' : info['barvlDt'],
                            'arvlMsg2' : info['arvlMsg2'],
                            'arvlMsg3' : info['arvlMsg3'],
                        })
            subway_infomation.append({'Munjung Station' : infomation})
            
            print(subway_infomation)
            return Response(subway_infomation, status=status.HTTP_200_OK)
        else:
            print("Error:", response.status_code)


class HomeJamsilToKonkuk(APIView):
    def get(self, request, format=None):
        BASE_DIR = Path(__file__).resolve().parent.parent
        secret_file = os.path.join(BASE_DIR, 'secret.json')

        with open(secret_file) as f:
            secrets = json.loads(f.read())

        subway_infomation = ["Ming's Subway to home"]
        base_url = "http://swopenapi.seoul.go.kr/api/subway/"
        subway_key = secrets['SUBWAY_KEY']
        url = base_url + subway_key + "/json/realtimeStationArrival/0/10/잠실"

        response = requests.get(url)
    
        if response.status_code == 200:
            infomation = []
            data = response.json()["realtimeArrivalList"]

            for info in data:
                subwayId = info['subwayId']
                trainLineNm = info['trainLineNm']

                if subwayId[-1] == '2':
                    if '잠실나루' in trainLineNm:
                        infomation.append({
                            'barvlDt' : info['barvlDt'],
                            'arvlMsg2' : info['arvlMsg2'],
                            'arvlMsg3' : info['arvlMsg3'],
                        })
            subway_infomation.append({'Jamsil To Konkuk Station' : infomation})
            
            print(subway_infomation)
            return Response(subway_infomation, status=status.HTTP_200_OK)
        else:
            print("Error:", response.status_code)


class HomeJamsilToSadang(APIView):
    def get(self, request, format=None):
        BASE_DIR = Path(__file__).resolve().parent.parent
        secret_file = os.path.join(BASE_DIR, 'secret.json')

        with open(secret_file) as f:
            secrets = json.loads(f.read())

        subway_infomation = ["Ming's Subway to home"]
        base_url = "http://swopenapi.seoul.go.kr/api/subway/"
        subway_key = secrets['SUBWAY_KEY']
        url = base_url + subway_key + "/json/realtimeStationArrival/0/10/잠실"

        response = requests.get(url)
    
        if response.status_code == 200:
            infomation = []
            data = response.json()["realtimeArrivalList"]

            for info in data:
                subwayId = info['subwayId']
                trainLineNm = info['trainLineNm']

                if subwayId[-1] == '2':
                    if '잠실새내' in trainLineNm:
                        infomation.append({
                            'barvlDt' : info['barvlDt'],
                            'arvlMsg2' : info['arvlMsg2'],
                            'arvlMsg3' : info['arvlMsg3'],
                        })
            subway_infomation.append({'Jamsil To Sadang Station' : infomation})
            
            print(subway_infomation)
            return Response(subway_infomation, status=status.HTTP_200_OK)
        else:
            print("Error:", response.status_code)