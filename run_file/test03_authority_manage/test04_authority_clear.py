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

    # 清空权限
    def test_create_authority(self, text="【权限清空】"):
        self.auth.click_text_authority_name()
        self.auth.click_powers_all()
        self.auth.click_powers_confirm()
        self.auth.selected_false(authority_manage.loc("authorization_success"), text)


if __name__ == '__main__':
    pytest.main(["-s", "test04_authority_clear.py"])
