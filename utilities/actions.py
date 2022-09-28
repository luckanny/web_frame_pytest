from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Actions:

    def __init__(self, driver):
        self.driver = driver

    def click(self, element):
        element.click()

    def sendkeys(self, inputfield, value):
        inputfield.send_keys(value)

    def selectfromDD(self, dropdown, value):
        ddelement = Select(dropdown)
        ddelement.select_by_value(value)

    def gettext(self, element):
        return element.text

    def isclickable(self,element):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(element))
            return True
        except:
            return False