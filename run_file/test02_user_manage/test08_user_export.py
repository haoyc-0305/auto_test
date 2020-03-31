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

    # 用户导出
    def test_user_export(self, file_name=data("user_export")):
        self.user_manage.click_user_export()
        self.user_manage.file_find(file_name)


if __name__ == '__main__':
    pytest.main(["-s", "test08_user_export.py"])