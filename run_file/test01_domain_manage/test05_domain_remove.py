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

    # 移除域用户
    def test_remove_user(self, text="【移除域用户】"):
        user_text = self.domain.get_text(domain_manage.loc("user_statistical"))
        self.domain.click_select_user()
        self.domain.click_remove_user()
        self.domain.click_confirm()
        self.domain.not_text_element(domain_manage.loc("user_statistical"), user_text, text)


if __name__ == '__main__':
    pytest.main(["-s", "test05_domain_remove.py"])