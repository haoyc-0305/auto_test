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

    # 下载导入模版
    def test_download_file(self):
        self.hardware.click_download_file()
        self.hardware.file_find(data("download_file"))

    # 导入模版
    def test_upload_file(self):
        device_number = self.hardware.get_text(hardware_manage.loc("device_number"))
        self.hardware.click_upload_file()
        self.hardware.file_upload(data("upload_file"))
        sleep(5)
        self.hardware.not_text_element(hardware_manage.loc("device_number"), device_number, "导入【%s】"
                                       % data("upload_file"))

    # 导出模版
    def test_export_file(self):
        self.hardware.click_export_file()
        self.hardware.file_find(data("export_file"))


if __name__ == '__main__':
    pytest.main(["-s", "test03_import_hardware.py"])