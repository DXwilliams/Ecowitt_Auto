#coding=utf-8
from pprint import pprint

from selenium import webdriver


driver = webdriver.Chrome()
url = "https://www.baidu.com/"
driver.get(url)
ListA=[]
Xpath="//div[@id='wrapper']/child::node()[1]"
A=driver.find_elements_by_xpath(Xpath)
ListA.append(A)
pprint(ListA)