from base_file.base_driver import setup, login
from base_file.base_yaml import data_yaml
from conf_file import my_application
import os, sys
sys.path.append(os.getcwd())
import pytest


def data(key):
    return data_yaml("data_my_application")[key]


class TestOpenApp:

    def setup_class(self):
        self.driver = setup()
        self.myapp = my_application.MyApplication(self.driver)
        login(self.driver, data("user_name"), data("user_pass"))

    def teardown_class(self):
        self.driver.quit()

    @pytest.mark.parametrize("soft_num", data("open_application"))
    def test_open_application(self, soft_num):
        self.myapp.open_application(soft_num)
        self.myapp.element_number(my_application.loc("connect_record"), int(soft_num) + 1,
                                  "打开软件【%s】" % self.myapp.loc_soft(soft_num))


if __name__ == '__main__':
    pytest.main(["-s", "test00_open_application.py"])
