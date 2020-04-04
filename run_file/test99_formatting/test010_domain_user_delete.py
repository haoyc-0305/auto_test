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
        # login(self.driver)
        # self.domain.open_domain()

    # 注销并关闭浏览器
    def teardown_class(self):
        self.driver.quit()

    # 删除域用户
    # def test_delete_user(self, user_name="haoyc0", text="【删除域用户】"):
    #     user_text = self.domain.get_text(domain_manage.loc("user_statistical"))
    #     self.domain.find_system_user(user_name)
    #     self.domain.click_find()
    #     self.domain.click_select_user()
    #     self.domain.click_delete_user()
    #     self.domain.click_confirm()
    #     self.domain.click_confirm()
    #     self.domain.not_text_element(domain_manage.loc("user_statistical"), user_text, text)

    # 清空域用户表
    def test_delete_system_user(self, sql=data("sql_delete_system_user")):
        self.domain.data_run(sql)


if __name__ == '__main__':
    pytest.main(["-s", "test010_domain_user_delete.py"])