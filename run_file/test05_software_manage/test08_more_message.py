import os, sys
from time import sleep

sys.path.append(os.getcwd())
import pytest
from base_file.base_driver import setup, login
from base_file.base_yaml import data_yaml
from conf_file import software_manage


def data(key):
    return data_yaml("data_software")[key]


class TestHardware:

    # 打开软件资源管理
    def setup_class(self):
        self.driver = setup()
        self.soft = software_manage.SoftwareManage(self.driver)
        login(self.driver)
        self.soft.open_soft_manage()

    def teardown_class(self):
        self.driver.quit()

    # 培训资料留言
    def test_message(self, massage=data("massage")):
        self.soft.input_search_input(massage["soft_name"])
        self.soft.click_more(massage["loc"])
        self.soft.click_massage()
        self.soft.input_massage(massage["massage"])
        self.soft.click_publish_massage()
        self.soft.displayed_true(software_manage.loc("massage_checkout"), "【管理员留言发表】")


if __name__ == '__main__':
    pytest.main(["-s", "test08_more_message.py"])