import os, json, requests
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
secret_file = os.path.join(BASE_DIR, 'secret.json')

with open(secret_file) as f:
    secrets = json.loads(f.read())

base_url = "http://swopenapi.seoul.go.kr/api/subway/"
subway_key = secrets['SUBWAY_KEY']
url = base_url + subway_key + "/json/realtimeStationArrival/0/10/"
subways = ["건대입구", "잠실", "문정", "사당"]
dic_eng = {
    "건대입구" : "Konkuk",
    "잠실" : "Jamsil",
    "문정" : "Munjeong",
    "사당" : "Sadang",
}

for subway in subways:
    response = requests.get(url + subway)
    if response.status_code == 200:
        data = response.json()
        print(type(data))
        
        with open('subway//mingway//realtimeSubway//' + dic_eng[subway] + '.json', 'w', encoding='utf-8') as f:
            json.dump(data["realtimeArrivalList"], f, ensure_ascii=False, indent=4)
    else:
        print("Error:", response.status_code)