import pytest
from base_file.base_driver import setup, login
from conf_file import user_manage
from base_file.base_yaml import data_yaml
import os, sys
sys.path.append(os.getcwd())


def data(key):
    return data_yaml("data_user_manage")[key]


class TestEditDepartment:

    def setup_class(self):
        self.driver = setup()
        self.user_manage = user_manage.UserManage(self.driver)
        login(self.driver)
        self.user_manage.open_user_manage()

    def teardown_class(self):
        self.driver.quit()

    # 编辑局级部门
    def test_department_edit_juji(self, department_data=data("test_edit_juji")):
        self.user_manage.click_director_edit_juji()
        self.user_manage.click_edit_department()
        self.user_manage.input_department_name(department_data[0])
        self.user_manage.input_email(department_data[1])
        self.user_manage.click_department_confirm()
        self.user_manage.displayed_true(user_manage.loc("edit_rank_juji"), "编辑局级【%s】" % department_data[0])

    # 编辑科级部门
    def test_department_edit_keji(self, department_data=data("test_edit_keji")):
        self.user_manage.click_director_edit_keji()
        self.user_manage.click_edit_department()
        self.user_manage.input_department_name(department_data)
        self.user_manage.click_rank_list()
        self.user_manage.click_rank_chuji(clear=1)
        self.user_manage.click_director()
        self.user_manage.click_edit_director_juji()
        self.user_manage.click_department_confirm()
        self.user_manage.displayed_true(user_manage.loc("edit_rank_chuji"), "编辑科级【%s】" % department_data)

    # 编辑处级部门
    def test_department_edit_chuji(self, department_data=data("test_edit_chuji")):
        self.user_manage.click_director_edit_chuji()
        self.user_manage.click_edit_department()
        self.user_manage.input_department_name(department_data)
        self.user_manage.click_rank_list()
        self.user_manage.click_rank_keji(clear=1)
        self.user_manage.click_director()
        self.user_manage.click_edit_director_chuji()
        self.user_manage.click_department_confirm()
        self.user_manage.displayed_true(user_manage.loc("edit_rank_keji"), "编辑处级【%s】" % department_data)


if __name__ == '__main__':
    pytest.main(["-s", "test02_department_edit.py"])