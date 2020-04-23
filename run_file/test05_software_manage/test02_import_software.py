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

    # 下载导入模版
    def test_download_file(self):
        self.soft.click_download_file()
        self.soft.file_find(data("download_file"))

    # 导入
    def test_upload_file(self):
        soft_number = self.soft.get_text(software_manage.loc("soft_number"))
        self.soft.click_upload_file()
        self.soft.file_upload(data("upload_file"), wait=2)
        self.soft.not_text_element(software_manage.loc("soft_number"), soft_number, "【软件导入】")

    # 导出
    def test_export_file(self):
        self.soft.click_export_file()
        self.soft.file_find(data("export_file"))


if __name__ == '__main__':
    pytest.main(["-s", "test02_import_software.py"])