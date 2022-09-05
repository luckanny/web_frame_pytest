import time

import allure
import pytest
from logs.log_main import logger
from po.load_page import LoadPage
from configure import web_constant
@pytest.fixture(scope="class")
def user_driver():
    logger.info("before class..will start web.");
    LoadPage().launch_url(web_constant.user_url)
    yield
    logger.info("after class..will close driver.");
    pass

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item,call):
    outcome = yield
    report = outcome.get_result()
    if report.when =="call":
        o = report.outcome
        s = f"用例执行结果 ：【{report.outcome}】"
        path = f"images/{time.time()}.png"
        if o == "failed":
            logger.error(s)
        elif o =="skip":
            logger.warning(s)
        else:
            logger.info(s)
        if "user_driver" in item.fixturenames:
            driver = item.funcargs["user_driver"]
            allure.attach(driver.get_screenshot_as_file(),"截图")
            driver.get_screenshot_as_file(path)
            logger.info(f"页面截图：{path}")


