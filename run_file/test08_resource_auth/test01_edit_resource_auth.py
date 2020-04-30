import os, sys
sys.path.append(os.getcwd())
import pytest
from base_file.base_driver import setup, login
from base_file.base_yaml import data_yaml
from conf_file import resource_auth


def data(key):
    return data_yaml("data_resource_auth")[key]


class TestResourceAuth:

    # 打开资源授权
    def setup_class(self):
        self.driver = setup()
        self.auth = resource_auth.ResourceAuth(self.driver)
        login(self.driver)
        self.auth.open_resource_auth()

    def teardown_class(self):
        self.driver.quit()

    # 编辑资源授权
    def test_edit_resource_auth(self):
        self.auth.input_search_input(data("edit_resource_auth"))
        self.auth.click_select_auth()
        self.auth.click_edit_resource()
        self.auth.click_edit_select_resource_group()
        self.auth.click_resource_auth_confirm()
        self.auth.displayed_true(resource_auth.loc("resource_group_name"), "编辑资源授权【%s】"
                                 % data("edit_resource_auth"))


if __name__ == '__main__':
    pytest.main(["-s", "test01_edit_resource_auth.py"])