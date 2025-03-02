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
JWT_KEY = "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1c2VyX25hbWUiOiJsaW5rZXI6MDYzZW02aWhwQG1vem1haWwuY29tIiwidXNlcl9pZCI6MTA0MjE4MDc1LCJpZGVudGl0eV9pZCI6MjA0NDQyMDEyLCJwcm92aWRlciI6ImRldmljZSIsImV4dGVybmFsX2lkIjoiV2luZG93cy0wMEM2RUFDQjQ1REUxRjVERTYxRTUyQTI2Q0YwNjZERiIsInBheW1lbnQiOiJub3RhdmFpbGFibGUiLCJyb2xlcyI6W10sImlhdCI6MTc0MDkxMjY5MCwiZXhwIjoxNzQwOTk5MDkwLCJqdGkiOiJwV3FXNjYxT1ptenhyTTcwM3lYRSIsImlzcyI6ImthcmRzLWJhY2tlbmQiLCJ0aWVyIjoiTElWRSIsImxhbmd1YWdlIjoiemgtSGFucyIsImNsaWVudF9pZCI6MTU2OTU2ODk5LCJwbGF5ZXJfaWQiOjQxODg2NTB9.KhSUsbRj_WIgwBv8CX97O-58mAN8aXeQbtTbSVAMOPrwZpfcYst8437FZbUAeko6I7FD0tLOQJjBffnoMbu6mPMGuvJX3-XMqT24VYCRRNnxPHBOxzfUlOVNx2zDLNjPJbFSellvmu4RNWspSYGNkOAXhSxxetCyZUyBvI8tNBPLOwJUNuAGHJfunZaohXuyCGTHRVlc_nfXB5RBwC-Dje08uyfAt9YDt4B0Qpn3nrv57URN-OXu-fsVzVngcP4JEERzgzpdYH-zYkEG0iVUDxNI2tW0bpgmm0plPdRMqwh8jd2leF9zj0Z4_0uTg3lJEK3uvn5WASXsmRomduaMXg"
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
def getJJCData(headers):   
    global JJCount
    JJCount=0
    jjcDataUrl = f"https://kards.live.1939api.com/draft/{playerID}"
    jjcData = requests.get(jjcDataUrl,headers=headers,verify=False)
    JJCount = jjcData.json().get("wins")
    cardCount = jjcData.json().get("cards")
    print("JJCount:",JJCount)
    print("cardCount:",cardCount)
    if JJCount == 0:
        return cardCount
    else:
        return JJCount
    
# print(type(getJJCData(headers)))