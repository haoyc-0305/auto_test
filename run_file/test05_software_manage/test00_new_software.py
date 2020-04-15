import os, sys
from time import sleep

sys.path.append(os.getcwd())
import pytest
from base_file.base_driver import setup, login
from base_file.base_yaml import data_yaml
from conf_file import software_manage


def data(key):
    return data_yaml("data_hardware")[key]


class TestHardware:

    # 打开硬件资源管理
    def setup_class(self):
        self.driver = setup()
        self.hardware = software_manage.SoftwareManage(self.driver)
        login(self.driver)
        self.hardware.open_hardware_manage()

    def teardown_class(self):
        self.driver.quit()

    # 新建硬件设备.
    @pytest.mark.parametrize("parameters", data("hardware_parameters"))
    def test_new_linux_hardware(self, parameters):


if __name__ == '__main__':
    pytest.main(["-s", "test00_new_hardware.py"])