import pytest
from selenium import webdriver
from pathlib import Path
from configure import web_constant
@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = web_constant.method
    ROOT_PATH = str(Path(__file__).parent.parent)
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path=ROOT_PATH + "/driver/chromedriver")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path=ROOT_PATH + "/driver/geckodriver")
    elif browser_name == "ie":
        driver = webdriver.Ie(executable_path=ROOT_PATH + "/driver/IEDriverServer.exe")
    driver.get(web_constant.user_url) # get the url from conf file
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()