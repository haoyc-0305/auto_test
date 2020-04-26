import os, sys
sys.path.append(os.getcwd())
import pytest
from time import sleep
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

    # 新建资源池
    @pytest.mark.parametrize("resource", data("new_resource_pool"))
    def test_new_resource(self, resource):
        resource_number = self.resource.get_text(resource_pool.loc("resource_number"))
        self.resource.click_new_resource_poll()
        self.resource.input_group_name(resource["group_name"])
        self.resource.click_type(resource["type"])
        self.resource.click_soft(resource["soft"])
        self.resource.input_describe(resource["describe"])
        self.resource.input_search(resource["node_name"])
        self.resource.click_node()
        self.resource.click_new_confirm()
        self.resource.not_text_element(resource_pool.loc("resource_number"), resource_number, "新建资源池【%s】"
                                     % resource["group_name"])


if __name__ == '__main__':
    pytest.main(["-s", "test00_new_resource_pool.py"])