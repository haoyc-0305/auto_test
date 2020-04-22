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

    # 新建硬件设备.
    @pytest.mark.parametrize("parameters", data("hardware_parameters"))
    def test_new_linux_hardware(self, parameters):
        self.driver.refresh()
        device_number = self.hardware.get_text(hardware_manage.loc("device_number"))
        self.hardware.click_new_hardware()
        self.hardware.click_system_type()
        self.hardware.click_system_types(parameters["system_type"])
        self.hardware.click_type()
        self.hardware.click_types(parameters["type"])
        self.hardware.input_out_ip(parameters["out_ip"])
        self.hardware.input_in_ip(parameters["in_ip"])
        self.hardware.input_describe(parameters["describe"])
        self.hardware.click_brand()
        self.hardware.click_brands(parameters["brand"])
        self.hardware.input_model(parameters["model"])
        self.hardware.input_sn(parameters["sn"])
        self.hardware.click_time()
        self.hardware.click_now()
        self.hardware.input_asset_num(parameters["asset_num"])
        self.hardware.click_warranty_time()
        self.hardware.click_two_years_warranty()
        self.hardware.click_subordinate_units()
        self.hardware.click_unit_juji()
        self.hardware.click_shutdown_unit_list()
        self.hardware.click_device_manager()
        self.hardware.click_device_admin()
        self.hardware.click_confirm()
        sleep(5)
        self.hardware.not_text_element(hardware_manage.loc("device_number"), device_number, "添加设备【%s】"
                                       % parameters["model"])


if __name__ == '__main__':
    pytest.main(["-s", "test00_new_hardware.py"])