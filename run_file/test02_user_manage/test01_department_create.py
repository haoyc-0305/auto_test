from time import sleep

import pytest
from base_file.base_driver import setup, login
from conf_file import user_manage
from base_file.base_yaml import data_yaml
import os, sys
sys.path.append(os.getcwd())


def data(key):
    return data_yaml("data_user_manage")[key]


class TestCreateDepartment:

    def setup_class(self):
        self.driver = setup()
        self.user_manage = user_manage.UserManage(self.driver)
        login(self.driver)
        self.user_manage.open_user_manage()

    def teardown_class(self):
        self.driver.quit()

    # 创建局级单位
    def test_create_juji(self, department_data=data("test_create_juji")):
        self.user_manage.click_create_department()
        self.user_manage.input_department_name(department_data[0])
        self.user_manage.click_rank_list()
        self.user_manage.click_rank_juji(clear=1)
        self.user_manage.input_email(department_data[1])
        self.user_manage.click_department_confirm()
        self.user_manage.element_number(user_manage.loc("department_list"), department_data[2],
                                        "创建局级【%s】" % department_data[0])

    # 创建处级单位
    def test_create_chuji(self, department_data=data("test_create_chuji")):
        self.user_manage.click_create_department()
        self.user_manage.input_department_name(department_data[0])
        self.user_manage.click_rank_list()
        self.user_manage.click_rank_chuji(clear=1)
        self.user_manage.click_director()
        self.user_manage.click_new_director_juji()
        self.user_manage.click_department_confirm()
        self.user_manage.element_number(user_manage.loc("department_list"), department_data[1],
                                        "创建处级【%s】" % department_data[0])

    # 创建科级单位
    def test_create_keji(self, department_data=data("test_create_keji")):
        self.user_manage.click_create_department()
        self.user_manage.input_department_name(department_data[0])
        self.user_manage.click_rank_list()
        self.user_manage.click_rank_keji(clear=1)
        self.user_manage.click_director()
        self.user_manage.click_new_director_chuji()
        self.user_manage.click_department_confirm()
        self.user_manage.element_number(user_manage.loc("department_list"), department_data[1],
                                        "创建科级【%s】" % department_data[0])


if __name__ == '__main__':
    pytest.main(["-s", "test01_department_create.py"])


