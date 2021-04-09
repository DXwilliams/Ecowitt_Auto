#coding=utf-8
import requests
import pandas
import openpyxl

#requests支持方法
# #home_post=requests.post(homedata_url)
# #print("status code",res_get.status_code)
# print("status code:",res_post.status_code)
# print("地址：",res_post.url)
# print("cookies:",res_post.cookies)
# print("headers",res_post.headers)
# print("text:",res_post.text)#html , json xml 结果都可以
#print("json:",res_post.json())#一定要json格式
# #print("home:",home_post.json())

#添加请求头
#headers={"":""}

login_url='https://webapi.www.ecowitt.net/user/site/login'
#homedata_url="https://webapi.www.ecowitt.net/index/home"
#res_get=requests.get(login_url)
data={'account':'462451569@qq2.com','password':'123456'}
# res_post1=requests.post(login_url)
# print(res_post1.json())
res_post=requests.post(login_url,data=data)


def visit_json(method,url,data,**kwargs):
    """访问http接口，得到json数据"""
    response = requests.request(
        method,
        url,
        #params=params,
        data=data,
        #json = json
        **kwargs
                                )
    Status_Code = response.status_code

    try:
        # 返回json数据和验证服务器状态码
        return (response.json(),Status_Code)
    except:
        # print(response)
        #print("不是json格式")
        return None

# R = visit_json("post",login_url,data)
# print(R)