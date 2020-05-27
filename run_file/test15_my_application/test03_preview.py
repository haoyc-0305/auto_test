from base_file.base_driver import setup, login
from base_file.base_yaml import data_yaml
from conf_file import my_application
import os, sys
sys.path.append(os.getcwd())
import pytest


def data(key):
    return data_yaml("data_my_application")[key]


class TestPreview:

    def setup_class(self):
        self.driver = setup()
        self.myapp = my_application.MyApplication(self.driver)
        login(self.driver, data("user_name"), data("user_pass"))

    def teardown_class(self):
        self.driver.quit()

    def test_preview(self):
        self.myapp.click_cultivate_material()
        self.myapp.click_preview()
        self.myapp.displayed_true(my_application.loc("preview_bounced"), "【培训资料-预览】")



if __name__ == '__main__':
    pytest.main(["-s", "test03_preview.py"])
