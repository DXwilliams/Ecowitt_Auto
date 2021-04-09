#coding=utf-8
import requests
import openpyxl
#import apitest     导入整个文件
from apitest import visit_json   #导入文件中的某个方法
import json


#1.打开excel=加载文件
#workbook ==＞ 工作簿

workbook = openpyxl.load_workbook("api_test.xlsx")
#print(workbook)
#2.打开后，获取表格sheet
sheet = workbook["demo"]   #可打开指定sheet
#sheet = workbook.active   #默认打开第一个sheet
#print(sheet)

#3.获取文件中的第2行，第2列（指定单元格）
#cell对象:数据只是单元格的一个属性，长宽高，颜色，背景色等等   <Worksheet "demo">
url = sheet.cell(3,2)
#print(url.value)



#4.获取所有行   <generator object Worksheet._cells_by_row at 0x11815FB0>   rows是一个生成器
rows = list(sheet.rows)  #把rows转化成list
#row代表，是excel中的某一行
for row in rows[1:]:
    method_get = row[3].value.encode("utf-8").decode("latin1")
    url_get = row[2].value.encode("utf-8").decode("latin1")
    #获取这一行的url
    form_data = row[5].value
    # str_P="str"
    # dict_P = {}    #可以做一个空类型，然后做对比
    if type(form_data).__name__ == "str":       #判断type类型
        form_data_get = json.loads(form_data)    #将str转成dict
        res = visit_json(method=method_get, url=url_get, data=form_data_get)
        print(res)
    elif type(form_data).__name__ == "dict":
        res = visit_json(method=method_get, url=url_get, data=form_data)
        print(res)
    else:
        print("form_data不是str,不是dict或者为空")

        #print(type(form_data_get))
        #print(form_data_get)
        #print(method_get,url_get,form_data_get)
        #res = visit_json(method=method_get,url=url_get,data=form_data_get)
        #res_state = requests.request(method=method_get,url=url_get,data=form_data_get)





# login_url='https://webapi.www.ecowitt.net/user/site/login'
# data={'account':'462451569@qq2.com','password':'123456'}
# print(type(data))
# res1 = visit_json("post",login_url,data=data)
# print(res1)

#访问接口
#apitest.visit_json(method=method_get,url=url_get,data=form_data_get)   #导入整个文件的话，需要这样才能用到方法
