import os, sys
sys.path.append(os.getcwd())
import pytest
from base_file.base_driver import setup, login
from base_file.base_yaml import data_yaml
from conf_file import resource_auth


def data(key):
    return data_yaml("data_resource_auth")[key]


class TestResourceAuth:

    # 打开资源授权
    def setup_class(self):
        self.driver = setup()
        self.auth = resource_auth.ResourceAuth(self.driver)
        login(self.driver)
        self.auth.open_resource_auth()

    def teardown_class(self):
        self.driver.quit()

    # 下载导入模版
    def test_download_file(self):
        self.auth.click_download_file()
        self.auth.file_find(data("download_file"))

    # 导入
    def test_import_file(self):
        auth_number = self.auth.get_text(resource_auth.loc("resource_auth_number"))
        self.auth.click_upload_file()
        self.auth.file_upload(data("import_file"), wait=2)
        self.auth.not_text_element(resource_auth.loc("resource_auth_number"), auth_number, "【导入资源授权】")

    # 导出
    def test_export_file(self):
        self.auth.click_export_file()
        self.auth.file_find(data("export_file"))


if __name__ == '__main__':
    pytest.main(["-s", "test02_import_resource_auth.py"])