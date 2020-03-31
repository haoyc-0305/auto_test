from time import sleep
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

    # 用户冻结
    def test_user_freeze(self, text="【用户冻结】"):
        self.user_manage.click_user_all()
        self.user_manage.click_user_freeze()
        self.user_manage.displayed_true(user_manage.loc("user_freeze"), text)

    # 用户解锁
    def test_user_unlock(self, text="【用户解锁】"):
        self.user_manage.click_user_all()
        self.user_manage.click_user_unlock()
        self.user_manage.displayed_true(user_manage.loc("user_unlock"), text)


if __name__ == '__main__':
    pytest.main(["-s", "test021_user_delete.py"])