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

    # 添加职权用户
    def test_create_authority(self, text="【添加职权用户】"):
        # 添加测试用户
        self.auth.click_test_authority_name()
        self.auth.click_authority_add_user()
        self.auth.click_authority_user_name()
        self.auth.click_confirm_select()
        # 添加应用管理员用户
        self.auth.click_app_authority_name()
        self.auth.click_authority_add_user()
        self.auth.click_authority_user_name()
        self.auth.click_confirm_select()
        # 添加设备管理员用户
        self.auth.click_device_authority_name()
        self.auth.click_authority_add_user()
        self.auth.click_authority_user_name()
        self.auth.click_confirm_select()
        # 添加系统管理员用户
        self.auth.click_system_authority_name()
        self.auth.click_authority_add_user()
        self.auth.click_authority_user_name()
        self.auth.click_confirm_select()
        self.auth.displayed_true(authority_manage.loc("authority_add_name"), text)


if __name__ == '__main__':
    pytest.main(["-s", "test02_authority_add_user.py"])
