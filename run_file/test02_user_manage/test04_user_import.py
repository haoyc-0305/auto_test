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

    # 下载导入模版
    def test_download_template(self, temp_name=data("download_name")):
        self.user_manage.click_download_template()
        self.user_manage.file_find(temp_name)

    # 导入用户
    def test_import_template(self, file_name=data("import_name")):
        user_number = self.user_manage.get_text(user_manage.loc("user_number"))
        self.user_manage.click_import_template()
        self.user_manage.file_upload(file_name)
        self.user_manage.not_text_element(user_manage.loc("user_number"), user_number,
                                          "【导入用户】")


if __name__ == '__main__':
    pytest.main(["-s", "test04_user_import.py"])