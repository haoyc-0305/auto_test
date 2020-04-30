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

    # 删除资源授权
    def test_delete_resource_auth(self):
        auth_number = self.auth.get_text(resource_auth.loc("resource_auth_number"))
        self.auth.click_select_auth()
        self.auth.click_delete()
        self.auth.click_delete_confirm()
        self.auth.not_text_element(resource_auth.loc("resource_auth_number"), auth_number, "【删除资源授权】")


if __name__ == '__main__':
    pytest.main(["-s", "test080_delete_resource_auth.py"])