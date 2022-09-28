from selenium.webdriver.common.by import By
from utilities.base import Base

class SearchPage(Base):

    def __init__(self, driver):
        self.driver = driver
        super().__init__()


    search_keyword = (By.CSS_SELECTOR,"input[id='kw']")
    search_button = (By.CSS_SELECTOR, "input[id='su']")


    def get_searchkeywork(self):
        self.get_logger().info(SearchPage.search_keyword)
        return self.driver.find_element(*SearchPage.search_keyword)

    def get_searchbutton(self):
        return self.driver.find_element(*SearchPage.search_button)