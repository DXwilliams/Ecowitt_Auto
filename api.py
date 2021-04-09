#coding=utf-8
import requests
import json
import time

def Login_api():
    login_url = 'https://webapi.www.ecowitt.net/user/site/login'
    shop_loginurl = "https://www.ecowitt.com/api/user/login"
    login_data={"account":"462451569@qq2.com","password":"123456"}
    shop_logindata = {"account": "462451569@qq2.com", "password":"123456", "keeplogin":"0"}
    #RES=requests.request("post",login_url,params=data)
    try:
        #post 以json格式传参
        #J=requests.post(login_url,json=data)
        #以form_data形式传参
        RES = requests.request("post", login_url, data=login_data)
        # print(RES.json())
        # print(RES.status_code)
        shop_RES = requests.request("post", shop_loginurl, json=login_data)
        print(shop_RES.json())

        #print(J.json())
        #print(RES.json()["errcode"])     #单独打印出其中的参数数据
    except:
        print("不是json格式")

def home_C():
    #保持登录状态
    session = requests.Session()
    login_url = 'https://webapi.www.ecowitt.net/user/site/login'
    login_data = {"account": "462451569@qq2.com", "password": "123456"}
    req_header ={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.7 Safari/537.36"}
    login_Session = session.post(login_url,headers=req_header,data=login_data)
    if login_Session.status_code ==200 :
        #print(login_Session.json())
        home_url = "https://webapi.www.ecowitt.net/index/home"
        home_data={"device_id":"14560"}
        try:
            home_res = session.request("post",home_url,data=home_data)
            device_data = home_res.json()["data"]
            print(home_res.status_code)

            batt = device_data["batt"]
            batt_data = batt["data"]
            print(batt_data["wh40batt"])

        except:
            print("不是json格式")



#def get_cookies():


Login_api()
#home_C()
