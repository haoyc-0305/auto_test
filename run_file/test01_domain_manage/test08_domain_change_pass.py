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

    # 搜索并修改密码
    def test_search_user(self, user_info=data("test_add_user")):
        self.domain.find_system_user(user_info[0])
        self.domain.click_find()
        self.domain.click_edit_pass()
        self.domain.input_pass0(user_info[1])
        self.domain.input_pass1(user_info[1])
        self.domain.confirm_pass()


if __name__ == '__main__':
    pytest.main(["-s", "test08_domain_change_pass.py"])