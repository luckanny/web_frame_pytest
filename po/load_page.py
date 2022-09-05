from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_webdriver import BaseWebdriver
from logs.log_main import logger
from configure import web_constant
import time

class LoadPage:

    def launch_url(self,url):
        logger.info(f"launchToURL: {url}");
        BaseWebdriver().open_homepage(url)

