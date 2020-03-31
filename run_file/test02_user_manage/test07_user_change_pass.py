import pytest
from base_file.base_driver import setup, login
from conf_file import user_manage
from base_file.base_yaml import data_yaml
import os, sys
sys.path.append(os.getcwd())


def data(key):
    return data_yaml("data_user_manage")[key]


class TestEditDepartment:

    def setup_class(self):
        self.driver = setup()
        self.user_manage = user_manage.UserManage(self.driver)
        login(self.driver)
        self.user_manage.open_user_manage()

    def teardown_class(self):
        self.driver.quit()

    # 用户搜索
    def test_user_freeze(self, username="haoyc02"):
        self.user_manage.input_user_find(username)

    # 修改密码
    def test_user_change_pass(self, user_pass=data("test_user_change_pass")):
        self.user_manage.click_user_all()
        self.user_manage.click_change_pass()
        self.user_manage.input_new_pass(user_pass)
        self.user_manage.input_confirm_pass(user_pass)
        self.user_manage.click_change_pass_confirm()


if __name__ == '__main__':
    pytest.main(["-s", "test07_user_change_pass.py"])