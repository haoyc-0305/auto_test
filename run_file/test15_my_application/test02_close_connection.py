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

    def test_close_connection(self):
        connection = self.myapp.get_text(my_application.loc("connection"))
        self.myapp.search_connection(data("search_name"))
        self.myapp.click_close()
        self.myapp.not_text_element(my_application.loc("connection"), connection, "关闭连接【%s】" % data("search_name"))


if __name__ == '__main__':
    pytest.main(["-s", "test02_close_connection.py"])
