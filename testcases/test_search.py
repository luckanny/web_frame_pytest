import time

from po.search import SearchPage
from utilities.actions import Actions
from utilities.base import Base
import pytest
@pytest.mark.usefixtures('setup')
class TestSearch():
    def test_search(self):
        log = Base().get_logger()
        sp = SearchPage(self.driver)
        actions = Actions(self.driver)
        actions.sendkeys(sp.get_searchkeywork(), "suzhou")
        log.info("search keyword")
        actions.click(sp.get_searchbutton())
        log.info("Clicked on search button")
        time.sleep(5)







