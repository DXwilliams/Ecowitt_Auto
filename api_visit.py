#coding=utf-8
import requests

def api_Test(method_T,url,form_Date,**kwargs):
    """访问http接口，得到json数据"""
    RES = requests.request(
        method_T,
        url,
        data=form_Date,
    **kwargs)

    try:
        return RES.json()
    except:
        return None



if __name__ == '__main__':
    # R = api_Test("post","https://webapi.www.ecowitt.net/user/site/login",{"account":"462451569@qq2.com","password":"123456"})
    # print(R)
    pass
