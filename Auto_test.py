
import unittest
from selenium import webdriver


class SearchBaidu(unittest.TestCase):
    def setUp(self):
        #建立浏览器对象,url
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.url='https://www.baidu.com/'

    def test_Baidu(self):
        #百度链接，打开百度链接
        brower=self.driver
        brower.get(self.url)
        input_Text = brower.find_element_by_id('kw')
        self.driver.implicitly_wait(30)
        input_Text.clear()
        input_Text.send_keys('自动化')
        self.driver.implicitly_wait(30)
        submit = brower.find_element_by_id('su')
        submit.click()
    def tearDown(self):
        self.driver.quit()




if __name__ =='__main__':
    unittest.main(verbosity=2)