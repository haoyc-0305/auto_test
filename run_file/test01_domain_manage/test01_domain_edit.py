import os, sys
sys.path.append(os.getcwd())
import pytest
from base_file.base_driver import setup, login
from conf_file import domain_manage
from base_file.base_yaml import data_yaml


def data(key):
    return data_yaml("domain_data")[key]


class TestDomain:

    # 打开浏览器并打开域管理
    def setup_class(self):
        self.driver = setup()
        self.domain = domain_manage.DomainManage(self.driver)
        login(self.driver)
        self.domain.open_domain()

    def teardown_class(self):
        # 注销并关闭浏览器
        self.driver.quit()

    def test_edit_domain(self, text="域描述已修改", text_name="【编辑域】"):
        # 编辑域
        self.domain.click_check_domain()
        self.domain.input_describe(text, clear=1)
        self.domain.click_edit_confirm()
        self.domain.text_element(domain_manage.loc("describe_loc"), text, text_name)


if __name__ == '__main__':
    pytest.main(["-s", "test01_domain_edit.py"])