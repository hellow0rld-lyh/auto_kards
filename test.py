import requests
import json
import time
import threading
import random
import urllib3
import sys

# 填写替换你的玩家ID
playerID = 4188650
# 填写替换你的卡组ID
deckID = 52080704
# 填写替换你的Cookie
cookie = "[Put your Cookie In Here]"
# 填写替换你的JWT_KEY
JWT_KEY = "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1c2VyX25hbWUiOiJsaW5rZXI6MDYzZW02aWhwQG1vem1haWwuY29tIiwidXNlcl9pZCI6MTA0MjE4MDc1LCJpZGVudGl0eV9pZCI6MjA0NDQyMDEyLCJwcm92aWRlciI6ImRldmljZSIsImV4dGVybmFsX2lkIjoiV2luZG93cy0wMEM2RUFDQjQ1REUxRjVERTYxRTUyQTI2Q0YwNjZERiIsInBheW1lbnQiOiJub3RhdmFpbGFibGUiLCJyb2xlcyI6W10sImlhdCI6MTc0MDc0OTM2OSwiZXhwIjoxNzQwODM1NzY5LCJqdGkiOiJiOXgzUE9FUURRd2hKWkpSclJFcyIsImlzcyI6ImthcmRzLWJhY2tlbmQiLCJ0aWVyIjoiTElWRSIsImxhbmd1YWdlIjoiemgtSGFucyIsImNsaWVudF9pZCI6MTU1MjI5ODE0LCJwbGF5ZXJfaWQiOjQxODg2NTB9.pQvpCdaFFoF0YY3BySxslN8kyKlcu-QITnHt5SlEihWfJoEtJ6eyn1FSG7SYwRToUmhVtda06VK7NpTewjxr1FAm8-0nxtOGaIE5fncp4X-elGqtAaOvwYEvw_Y2vmQ0vIaAtaT-t02jQN82j2Fm5Hm21sbCQ7kcSj7lBLxgJ0xdiLQ_p-5N_sqdHY9MC0hW-MKjT0-404zZJG-i2vr2HrN6z2HDWLDgoqTfIW04Zn4bRANrifgnb7INhiFz4AJYkfGadOMlzwfB4JTrBcd-MVd7l8YcJNtSe3p9p1nn8H0k0kR0Z8sUq6Bec3-E1BWQmp36bL-CKoVUR6DKX1Mqhg"
urllib3.disable_warnings()
headers = {
    # 'Drift-Api-Key': '1939-kards-5dcba429f:Kards 1.15.16724.Steam',
    # 'X-Api-Key': '1939-kards-5dcba429f:Kards 1.15.16724.Steam',
    # 'Authorization': cookie,
    # # 'User-Agent': 'kards/++UE5+Release-5.2-CL-26001984 Windows/10.0.19045.1.256.64bit'
    "Accept-Encoding": "deflate, gzip",
    "Accept": "application/json",
    "X-Api-Key": "1939-kards-5dcba429f:Kards 1.29.20338.launcher",
    "Drift-Api-Key": "1939-kards-5dcba429f:Kards 1.29.20338.launcher",
    "Authorization": JWT_KEY,
    "Content-Type": "application/json",
    "User-Agent": "kards/++UE5+Release-5.4-CL-35576357 (http-legacy) Windows/10.0.19044.1.256.64bit",
}


def beginJJC(headers):
    beginJJCURL = f"https://kards.live.1939api.com/draft/{playerID}"
    data = {}
    headers.update({"Content-Type": "application/x-www-form-urlencoded"})
    response = requests.post(beginJJCURL, headers=headers, json=data, verify=False)
    if response.status_code == 200:
        # print("请求成功！")
        pass
        print("响应内容：", response.text)
        # return response.text
    else:
        # print("请求失败！")
        pass
        # print("状态码：", response.status_code)
        print("响应内容：", response.text)
    time.sleep(1)


def getJWTKey(headers):
    getJWTKeyURL = f"https://kards.live.1939api.com/session"
    headers.pop("Authorization")
    data = {
        "provider": "device_id",
        "provider_details": {"payment_provider": "XSOLLA"},
        "client_type": "UE5",
        "build": "Kards 1.29.20338.launcher",
        "platform_type": "Windows",
        "app_guid": "Kards",
        "version": "Kards 1.29.20338.launcher",
        "platform_info": '{\r\n\t"device_profile": "Windows",\r\n\t"cpu_vendor": "GenuineIntel",\r\n\t"cpu_brand": "Intel(R) Core(TM) i5-8265U CPU @ 1.60GHz",\r\n\t"gpu_brand": "Intel(R) UHD Graphics 620",\r\n\t"num_cores_physical": 4,\r\n\t"num_cores_logical": 8,\r\n\t"physical_memory_gb": 8,\r\n\t"hash": "2d40d993c9c37c1c70cfcccf72a0eaf44a18f487f5e66d2f8a5e6004a1ca6d21",\r\n\t"locale": "zh-CN"\r\n}',
        "platform_version": "Windows 10 (21H2) [10.0.19044.5487] ",
        "account_linking": "",
        "language": "zh-Hans",
        "automatic_account_creation": "true",
        "username": "device:Windows-00C6EACB45DE1F5DE61E52A26CF066DF",
        "password": "6F56CE9C4F1163FE027105B3A5813DEC",
    }
    response = requests.post(getJWTKeyURL, headers=headers, json=data, verify=False)
    if response.status_code == 200:
        print("请求成功！")
        pass
        # print("响应内容：", response.json())
        JWT_KEY = response.json().get("jwt")
        headers.update({"Authorization": JWT_KEY})  # 更新JWT_KEY
        print("JWT_KEY:", JWT_KEY)
        return response.text
    else:
        # print("请求失败！")
        pass
        # print("状态码：", response.status_code)
        print("响应内容：", response.text)

# getJWTKey(headers)
xxx=requests.get("https://raw.githubusercontent.com/hellow0rld-lyh/kardsRest/refs/heads/main/isTimeToRest")
print(xxx.text)
# createJJCURL = f"https://kards.live.1939api.com/draft/{playerID}/deck/create"
# while True:
#             data = {"pick":1}
#             headers.update({'Content-Type': 'application/json'})
#             response = requests.put(createJJCURL,headers=headers,json=data,verify=False)
#             if response.status_code == 200:
#                 print("请求成功！")
#                 print("响应内容：", response.text)
#             else:
#                 print("请求失败！")
#                 print("响应内容：", response.text)
#             if response.json().get("card_count") == 40:
#                 break
#             time.sleep(0.5)
