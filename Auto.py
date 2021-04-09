from selenium import webdriver
import requests

iccid = []
imei = []
iccid_1 = 8988303000004850000
imei_1 = 863879043570000
for x in range(10):
    iccid_1+=1
    iccid.append(iccid_1)
#print(iccid)
for i in range(10):
    imei_1+=1
    imei.append(imei_1)
#print(imei)


def req_Get(iccid_n,imei_n):
    for j in iccid:
        for k in imei:
            url = 'https://api.ecowitt.net/api/emnify/v1/activate?'
            param = {iccid:iccid_n,imei:imei_n}
            req_get = requests.request('get',url,params=param)

