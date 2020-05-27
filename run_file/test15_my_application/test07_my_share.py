from base_file.base_driver import setup, login
from base_file.base_yaml import data_yaml
from conf_file import my_application
import os, sys
sys.path.append(os.getcwd())
import pytest


def data(key):
    return data_yaml("data_my_application")[key]


class TestMyShare:

    def setup_class(self):
        self.driver = setup()
        self.myapp = my_application.MyApplication(self.driver)
        login(self.driver, data("user_name"), data("user_pass"))
        self.myapp.click_my_share()

    def teardown_class(self):
        self.driver.quit()

    def test_my_share(self):
        self.myapp.click_share()
        self.myapp.click_share_department()
        self.myapp.displayed_true(my_application.loc("share_verify"), "【连接分享】")


if __name__ == '__main__':
    pytest.main(["-s", "test07_my_share.py"])
