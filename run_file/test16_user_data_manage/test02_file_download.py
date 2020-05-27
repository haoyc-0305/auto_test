from base_file.base_driver import setup, login
from base_file.base_yaml import data_yaml
from conf_file import user_data_manage
import os, sys
sys.path.append(os.getcwd())
import pytest


def data(key):
    return data_yaml("data_user_data_manage")[key]


class TestFileDownload:

    def setup_class(self):
        self.driver = setup()
        self.data_manage = user_data_manage.UserDataManage(self.driver)
        login(self.driver, data("user_name"), data("user_pass"))
        self.data_manage.open_user_data_manage()

    def teardown_class(self):
        self.driver.quit()

    def test_file_download(self):
        self.data_manage.click_soft_store()
        self.data_manage.click_select_file()
        self.data_manage.click_download(data("file_upload"))


if __name__ == '__main__':
    pytest.main(["-s", "test02_file_download.py"])