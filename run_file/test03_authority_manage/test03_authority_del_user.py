import os, sys
sys.path.append(os.getcwd())
import pytest
from base_file.base_driver import setup, login
from conf_file import authority_manage
from base_file.base_yaml import data_yaml


def data(key):
    return data_yaml("data_authority")[key]


class TestAuthority:

    # 打开职权管理
    def setup_class(self):
        self.driver = setup()
        self.auth = authority_manage.AuthorityManage(self.driver)
        login(self.driver)
        self.auth.open_authority()

    def teardown_class(self):
        self.driver.quit()

    # 移除职权用户
    def test_create_authority(self, text="【移除职权用户】"):
        self.auth.click_authority_del_select()
        self.auth.click_authority_del_user_select()
        self.auth.click_authority_del_user_confirm()
        self.auth.displayed_true(authority_manage.loc("test_authority_name"), text)


if __name__ == '__main__':
    pytest.main(["-s", "test03_authority_del_user.py"])
