import os, sys
sys.path.append(os.getcwd())
import pytest
from base_file.base_driver import setup, login
from conf_file import domain_manage
from base_file.base_yaml import data_yaml


def data(key):
    return data_yaml("data_domain")[key]


class TestDomain:

    # 打开浏览器并打开域管理
    def setup_class(self):
        self.driver = setup()
        self.domain = domain_manage.DomainManage(self.driver)
        login(self.driver)
        self.domain.open_domain()

    # 注销并关闭浏览器
    def teardown_class(self):
        self.driver.quit()

    # 下载导入模板
    def test_download_file(self):
        self.domain.download_file()
        self.domain.file_find(data("download_file_name"))

    # 导入模板
    # def test_find_upload(self, file_name=data("import_file"), text="【导入域用户】"):
    #     user_text = self.domain.get_text(domain_manage.loc("user_statistical"))
    #     self.domain.upload_file()
    #     self.domain.file_upload(file_name)
    #     self.domain.not_text_element(domain_manage.loc("user_statistical"), user_text, text)


if __name__ == '__main__':
    pytest.main(["-s", "test04_domain_import.py"])