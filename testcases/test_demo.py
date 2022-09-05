import pytest
# from logs.log_main1 import logger
from logs.log_main import logger
# logging.config.fileConfig("../logs/logging.conf")
# logger = logging.getLogger("applog")
@pytest.mark.usefixtures('after_class')
@pytest.mark.usefixtures('setup_class')
class TestWritePerformance:
    @pytest.mark.smoke
    def test_positive(self):
        print("111")







