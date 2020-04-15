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

    # 删除所有设备
    def test_del_hardware(self):
        device_number = self.hardware.get_text(hardware_manage.loc("device_number"))
        self.hardware.click_select_all()
        self.hardware.click_delete()
        self.hardware.click_update_confirm()
        self.hardware.not_text_element(hardware_manage.loc("device_number"), device_number, "【删除硬件资源】")


if __name__ == '__main__':
    pytest.main(["-s", "test040_del_hardware.py"])