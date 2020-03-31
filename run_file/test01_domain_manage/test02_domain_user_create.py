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

    # 创建域用户
    def test_add_user(self, text_data=data("test_add_user"), text_name="【创建域用户】"):
        self.domain.click_new_domain_user()
        self.domain.input_system_user_name(text_data[0])
        self.domain.input_system_user_pass(text_data[1])
        self.domain.input_system_user_id(text_data[2])
        self.domain.input_system_user_group_id(text_data[2])
        self.domain.input_system_user_home(text_data[3])
        self.domain.input_system_user_describe(text_data[0])
        self.domain.click_system_user_confirm()
        sleep(5)
        self.domain.text_element(domain_manage.loc("user_name_loc"), text_data[0], text_name)


if __name__ == '__main__':
    pytest.main(["-s", "test02_domain_user_create.py"])