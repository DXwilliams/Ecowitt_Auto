from selenium import webdriver
from time import sleep

def test_Baidu(url):
    # 百度链接，打开百度链接
    brower = webdriver.Chrome()
    brower.get(url)
    input_Text = brower.find_element_by_id('kw')
    brower.implicitly_wait(30)
    input_Text.clear()
    input_Text.send_keys('自动化')
    brower.implicitly_wait(30)
    submit = brower.find_element_by_id('su')
    submit.click()






test_Baidu('https://www.baidu.com/')