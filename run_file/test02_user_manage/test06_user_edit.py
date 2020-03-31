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

    # 编辑用户
    def test_user_freeze(self, text="【用户编辑】"):
        self.user_manage.click_select_keji()
        user_number = self.user_manage.get_text(user_manage.loc("user_number"))
        self.user_manage.click_user_edit()
        self.user_manage.click_unit_list()
        self.user_manage.click_unit_chuji()
        self.user_manage.click_user_create_confirm()
        self.user_manage.not_text_element(user_manage.loc("user_number"), user_number, text)


if __name__ == '__main__':
    pytest.main(["-s", "test06_user_edit.py"])