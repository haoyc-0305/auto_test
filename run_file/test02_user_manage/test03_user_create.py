from time import sleep
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

    # 创建用户
    def test_user_create(self, user_data=data("test_user_create")):
        user_number = self.user_manage.get_text(user_manage.loc("user_number"))
        self.user_manage.click_user_create()
        self.user_manage.input_user_name(user_data["user_name"])
        self.user_manage.input_name(user_data["name"])
        self.user_manage.click_unit_list()
        self.user_manage.click_unit_keji()
        self.user_manage.click_man()
        self.user_manage.input_ip_address(user_data["ip"])
        self.user_manage.input_mac_address(user_data["mac"])
        self.user_manage.input_tel(user_data["tel"])
        self.user_manage.input_mobile(user_data["mobile"])
        self.user_manage.click_ad()
        self.user_manage.click_nis()
        self.user_manage.click_user_create_confirm()
        sleep(5)
        self.user_manage.not_text_element(user_manage.loc("user_number"), user_number,
                                          "创建用户【%s】" % user_data["user_name"])


if __name__ == '__main__':
    pytest.main(["-s", "test03_user_create.py"])