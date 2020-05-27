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

    def test_my_share_open(self):
        connection = self.myapp.get_text(my_application.loc("share_connection"))
        self.myapp.click_my_share_close()
        self.myapp.not_text_element(my_application.loc("share_connection"), connection, "【我的分享-关闭】")


if __name__ == '__main__':
    pytest.main(["-s", "test06_my_share_close.py"])
