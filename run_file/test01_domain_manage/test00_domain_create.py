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

    # 创建AD域
    def test_new_ad(self, text=data("test_new_ad")):
        self.domain.click_new_domain()
        self.domain.input_domain_name(text[0])
        self.domain.click_domain_class()
        self.domain.click_domain_ad(clear=1)
        self.domain.input_domain_master_ip(text[1])
        self.domain.input_domain_user(text[2])
        self.domain.input_domain_pass(text[3])
        self.domain.input_domain_slave_ip(text[4])
        self.domain.input_domain_describe(text[0])
        self.domain.click_new_confirm()
        self.domain.displayed_true(domain_manage.loc("domain_ad_loc"), "创建AD域【%s】" % text[0])

    # 创建NIS域
    def test_new_nis(self, text=data("test_new_nis")):
        self.domain.click_new_domain()
        self.domain.input_domain_name(text[0])
        self.domain.click_domain_class()
        self.domain.click_domain_nis(clear=1)
        self.domain.input_domain_master_ip(text[1])
        self.domain.input_domain_user(text[2])
        self.domain.input_domain_pass(text[3])
        self.domain.input_domain_slave_ip(text[4])
        self.domain.input_domain_describe(text[0])
        self.domain.click_new_confirm()
        self.domain.displayed_true(domain_manage.loc("domain_nis_loc"), "创建NIS域【%s】" % text[0])


if __name__ == '__main__':
    pytest.main(["-s", "test00_domain_create.py"])