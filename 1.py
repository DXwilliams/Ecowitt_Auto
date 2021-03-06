# coding=utf-8
import requests
from test_openpyxl import read_excel
from api_visit import api_Test
from pprint import pprint

# h=获取所有的测试用例


def test_Ecowitt_01():
    Excel_D = read_excel("api_practice.xlsx", "demo")
    # pprint(Excel_D)
    row_01 = Excel_D[9]
    if not row_01[4] is None:
        Data = eval(row_01[4])
        session = requests.Session()
        login_url = "https://webapi.www.ecowitt.net/user/site/login"
        login_data = {"account": "462451569@qq2.com", "password": "123456"}
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.7 Safari/537.36"}
        Login_Session = session.post(login_url, headers=header, data=login_data)
        repsonse = api_Test(
            method_T=row_01[3],
            url=row_01[2],
            form_Date=Data
        )
        print(repsonse)
        expected = row_01[5]
        # print(repsonse['errcode'])
        # print(eval(expected)['errcode'])
        # print(type(repsonse['errcode']))
        assert repsonse['errcode'] == eval(expected)['errcode']


if __name__ == '__main__':
    R = test_Ecowitt_01()
    print(R)
    # pass
