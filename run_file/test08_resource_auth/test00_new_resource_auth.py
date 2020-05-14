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

    # 新建资源授权
    @pytest.mark.parametrize("auth", data("new_resource_auth"))
    def test_new_resource_auth(self, auth):
        auth_number = self.auth.get_text(resource_auth.loc("resource_auth_number"))
        self.auth.click_new_resource_auth()
        self.auth.click_select_user()
        self.auth.input_new_search_input(auth["soft_name"])
        self.auth.click_select_soft()
        self.auth.click_select_resource_group()
        self.auth.click_resource_auth_confirm()
        self.auth.not_text_element(resource_auth.loc("resource_auth_number"), auth_number, "创建授权【%s】"
                                   % auth["soft_name"])


if __name__ == '__main__':
    pytest.main(["-s", "test00_audit_config.py"])