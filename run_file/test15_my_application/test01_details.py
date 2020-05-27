from base_file.base_driver import setup, login
from base_file.base_yaml import data_yaml
from conf_file import my_application
import os, sys
sys.path.append(os.getcwd())
import pytest


def data(key):
    return data_yaml("data_my_application")[key]


class TestDetails:

    def setup_class(self):
        self.driver = setup()
        self.myapp = my_application.MyApplication(self.driver)
        login(self.driver, data("user_name"), data("user_pass"))

    def teardown_class(self):
        self.driver.quit()

    def test_details(self):
        self.myapp.search_connection(data("search_name"))
        self.myapp.click_details()
        self.myapp.displayed_true(my_application.loc("details_popout"), "【连接详情】")


if __name__ == '__main__':
    pytest.main(["-s", "test01_details.py"])
