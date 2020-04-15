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

    # 更新硬件设备
    def test_update_hardware(self):
        self.hardware.data_run(data("sql"))
        self.hardware.click_select_all()
        self.hardware.click_update_hardware()
        self.hardware.click_update_confirm()
        sleep(5)
        self.hardware.element_number(hardware_manage.loc("mac_text"), 0, "更新【所有设备】")


if __name__ == '__main__':
    pytest.main(["-s", "test02_update_hardware.py"])