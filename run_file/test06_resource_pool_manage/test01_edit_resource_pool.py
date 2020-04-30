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

    # 编辑资源池
    def test_new_resource(self, pool=data("edit_resource_pool")):
        self.resource.click_resource_pool()
        self.resource.input_edit_resource(pool["edit_describe"])
        self.resource.input_search(pool["node_name"])
        self.resource.click_node()
        self.resource.click_new_confirm()
        self.resource.displayed_true(resource_pool.loc("loc_describe"), "编辑资源池【%s】" % pool["pool_name"])


if __name__ == '__main__':
    pytest.main(["-s", "test01_edit_resource_pool.py"])