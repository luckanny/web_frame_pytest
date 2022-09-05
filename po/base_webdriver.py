import logging
import time

from selenium import webdriver
from configure import web_constant

class BaseWebdriver(object):
    def __int__(self):
        self.selenium_driver = self.start_webdriver()

    def start_webdriver(self):
        if web_constant.method=="chrome":
            selenium_driver = webdriver.Chrome(web_constant.chromedriver_path)
            selenium_driver.maximize_window()
            selenium_driver.implicitly_wait(10)
            return selenium_driver

    def open_homepage(self,url):
        selenium_driver=self.start_webdriver()
        selenium_driver.get(url)
        time.sleep(10)

    def stop_webdriver(self):
        try:
            self.selenium_driver.close()
        except Exception as e:
            logging.exception(e)


# driver = BrowserEngine().get_driver()
# driver.get("https://www.baidu.com")
# driver.close()