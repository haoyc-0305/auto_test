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

    # 删除资源池
    def test_delete_resource_pool(self):
        resource_number = self.resource.get_text(resource_pool.loc("resource_number"))
        self.resource.click_select_all()
        self.resource.click_delete_button()
        self.resource.click_delete_confirm()
        self.resource.not_text_element(resource_pool.loc("resource_number"), resource_number, "【删除资源池】")


if __name__ == '__main__':
    pytest.main(["-s", "test060_delete_resource_pool.py"])