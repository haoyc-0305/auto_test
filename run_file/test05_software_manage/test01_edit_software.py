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

    # 编辑软件
    def test_edit_software(self, soft=data("edit_software")):
        self.soft.click_edit_software()
        self.soft.click_new_soft_load(soft[1])
        self.soft.click_edit_confrim()
        self.soft.element_number(software_manage.loc("load_class_num"), 3, "编辑软件【%s】" % soft[0])


if __name__ == '__main__':
    pytest.main(["-s", "test01_edit_software.py"])