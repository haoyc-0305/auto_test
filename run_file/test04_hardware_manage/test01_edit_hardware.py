import os, sys
from time import sleep

sys.path.append(os.getcwd())
import pytest
from base_file.base_driver import setup, login
from base_file.base_yaml import data_yaml
from conf_file import hardware_manage


def data(key):
    return data_yaml("data_hardware")[key]


class TestHardware:

    # 打开硬件资源管理
    def setup_class(self):
        self.driver = setup()
        self.hardware = hardware_manage.HardwareManage(self.driver)
        login(self.driver)
        self.hardware.open_hardware_manage()

    def teardown_class(self):
        self.driver.quit()

    # 编辑硬件设备
    def test_edit_hardware(self):
        self.hardware.click_edit_hardware()
        self.hardware.input_describe(data("edit_hardware"))
        self.hardware.click_confirm()
        self.hardware.displayed_true(hardware_manage.loc("describe_text"), "编辑设备【%s】" %
                                     self.hardware.get_text(hardware_manage.loc("edit_hardware")))


if __name__ == '__main__':
    pytest.main(["-s", "test01_edit_hardware.py"])