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

    # 搜索
    def test_search(self):
        self.hardware.input_search_input(data("search_name"))

    # 停用设备
    def test_block_up(self):
        self.hardware.click_block_up()
        self.hardware.displayed_true(hardware_manage.loc("start"), "停用【%s】" % data("search_name"))

    # 启用设备
    def test_start(self):
        self.hardware.click_start()
        self.hardware.displayed_true(hardware_manage.loc("block_up"), "启用【%s】" % data("search_name"))


if __name__ == '__main__':
    pytest.main(["-s", "test04_search_block.py"])