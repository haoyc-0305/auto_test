import pytest
from base_file.base_driver import setup, login
from conf_file import user_manage
from base_file.base_yaml import data_yaml
import os, sys
sys.path.append(os.getcwd())


def data(key):
    return data_yaml("data_user_manage")[key]


class TestDeleteDepartment:

    def setup_class(self):
        self.driver = setup()
        self.user_manage = user_manage.UserManage(self.driver)
        login(self.driver)
        self.user_manage.open_user_manage()

    def teardown_class(self):
        self.driver.quit()

    # 删除科级部门
    def test_department_delete_keji(self, department_data=data("test_delete_keji")):
        self.user_manage.click_edit_rank_keji()
        self.user_manage.click_edit_department()
        self.user_manage.click_delete_department()
        self.user_manage.click_delete_department_confirm()
        self.user_manage.click_delete_department_confirm()
        self.user_manage.element_number(user_manage.loc("department_list"), department_data[1],
                                        "删除科级【%s】" % department_data[0])

    # 删除处级部门
    def test_department_delete_chuji(self, department_data=data("test_delete_chuji")):
        self.user_manage.click_edit_rank_chuji()
        self.user_manage.click_edit_department()
        self.user_manage.click_delete_department()
        self.user_manage.click_delete_department_confirm()
        self.user_manage.click_delete_department_confirm()
        self.user_manage.element_number(user_manage.loc("department_list"), department_data[1],
                                        "删除处级【%s】" % department_data[0])

    # 删除局级部门
    def test_department_delete_juji(self, department_data=data("test_delete_juji")):
        self.user_manage.click_edit_rank_juji()
        self.user_manage.click_edit_department()
        self.user_manage.click_delete_department()
        self.user_manage.click_delete_department_confirm()
        self.user_manage.click_delete_department_confirm()
        self.user_manage.element_number(user_manage.loc("department_list"), department_data[1],
                                        "删除局级【%s】" % department_data[0])


if __name__ == '__main__':
    pytest.main(["-s", "test022_department_delete.py"])