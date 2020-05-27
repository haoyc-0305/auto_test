from base_file.base_driver import setup, login
from base_file.base_yaml import data_yaml
from conf_file import my_application
import os, sys
sys.path.append(os.getcwd())
import pytest


def data(key):
    return data_yaml("data_my_application")[key]


class TestDownload:

    def setup_class(self):
        self.driver = setup()
        self.myapp = my_application.MyApplication(self.driver)
        login(self.driver, data("user_name"), data("user_pass"))

    def teardown_class(self):
        self.driver.quit()

    def test_download(self):
        self.myapp.click_cultivate_material()
        self.myapp.click_download()
        self.myapp.file_find(data("file_name"))


if __name__ == '__main__':
    pytest.main(["-s", "test04_download.py"])
