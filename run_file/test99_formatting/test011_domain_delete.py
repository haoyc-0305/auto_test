import os, sys
sys.path.append(os.getcwd())
import pytest
from base_file.base_driver import setup, login
from conf_file import domain_manage
from base_file.base_yaml import data_yaml


def data(key):
    return data_yaml("domain_data")[key]


class TestDomain:

    def setup_class(self):
        # 创建对象接受setup的返回值
        self.driver = setup()
        # 创建对象将self.driver传给DomainPage
        self.domain = domain_manage.DomainManage(self.driver)
        login(self.driver)

    # 注销并关闭浏览器
    def teardown_class(self):
        # 注销并关闭浏览器
        self.driver.quit()

    # 打开域管理
    def test_open_domain(self):
        self.domain.open_domain()

    # 删除所有域
    def test_delete_domain(self, text_name="【删除域】"):
        self.domain.click_all_domain(clear=1)
        self.domain.click_delete_domain()
        self.domain.click_confirm()
        self.domain.element_number(domain_manage.loc("domain_list"), "0", text_name)


if __name__ == '__main__':
    pytest.main(["-s", "test011_domain_delete.py"])