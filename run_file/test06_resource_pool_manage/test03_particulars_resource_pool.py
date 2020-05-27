import os, sys
sys.path.append(os.getcwd())
import pytest
from base_file.base_driver import setup, login
from base_file.base_yaml import data_yaml
from conf_file import resource_pool


def data(key):
    return data_yaml("data_resource_pool")[key]


class TestResourcePool:

    # 打开软件资源管理
    def setup_class(self):
        self.driver = setup()
        self.resource = resource_pool.ResourcePool(self.driver)
        login(self.driver)
        self.resource.open_resource_pool()

    def teardown_class(self):
        self.driver.quit()

    # 详情
    def test_particulars(self, particulars=data("edit_resource_pool")):
        self.resource.input_search_input(particulars["pool_name"])
        self.resource.click_particulars()
        self.resource.displayed_true(resource_pool.loc("loc_particulars"), "打开【%s】详情" % particulars["pool_name"])


if __name__ == '__main__':
    pytest.main(["-s", "test03_particulars_resource_pool.py"])