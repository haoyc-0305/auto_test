import os, sys
sys.path.append(os.getcwd())
import pytest
from base_file.base_driver import setup, login
from base_file.base_yaml import data_yaml
from conf_file import resource_pool


def data(key):
    return data_yaml("data_resource_pool")[key]


class TestResourcePool:

    # 打开软件资源管理
    def setup_class(self):
        self.driver = setup()
        self.resource = resource_pool.ResourcePool(self.driver)
        login(self.driver)
        self.resource.open_resource_pool()

    def teardown_class(self):
        self.driver.quit()

    # 下载导入模版
    def test_download_file(self):
        self.resource.click_download_file()
        self.resource.file_find(data("download_file"))

    # 导入模版
    def test_import_file(self):
        resource_number = self.resource.get_text(resource_pool.loc("resource_number"))
        self.resource.click_upload_file()
        self.resource.file_upload(data("import_file"), wait=2)
        self.resource.not_text_element(resource_pool.loc("resource_number"), resource_number, "【导入资源池】")

    # 导出资源池
    def test_export_file(self):
        self.resource.click_export_file()
        self.resource.file_find(data("export_file"))


if __name__ == '__main__':
    pytest.main(["-s", "test02_import_resource_pool.py"])