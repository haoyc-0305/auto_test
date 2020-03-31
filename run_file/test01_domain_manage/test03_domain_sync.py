import os, sys
sys.path.append(os.getcwd())
import pytest
from base_file.base_driver import setup, login
from conf_file import domain_manage
from base_file.base_yaml import data_yaml
from time import sleep


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

    # 同步域用户
    def test_import_domain_user(self, text="【同步域用户】"):
        self.domain.click_loading_user()
        self.domain.click_confirm()
        sleep(5)
        self.domain.element_number(domain_manage.loc("user_number"), "10", text)


if __name__ == '__main__':
    pytest.main(["-s", "test03_domain_sync.py"])