import os, sys
from base_file.base_yaml import data_yaml
sys.path.append(os.getcwd())
import pytest
from base_file.base_driver import setup, login, teardown
from conf_file import login_page

def data(key):
    return data_yaml("data_login")[key]

class TestLogin:

    def setup(self):
        self.driver = setup()
        self.login = login_page.LoginPage(self.driver)

    def teardown(self):
        self.driver.quit()

    def test_change_pass(self, lod_pass="111111", new_pass="222222"):
        admin_pass = self.login.data_run(data("admin_pass"))
        login(self.driver)
        self.login.change_pass()
        self.login.input_lod_pass(lod_pass)
        self.login.input_new_pass(new_pass)
        self.login.input_confirm_pass(new_pass)
        self.login.click_confirm_change()
        print("【修改密码】", self.login.data_run(data("admin_pass")) != admin_pass)

    def test_restore_pass(self, lod_pass="222222", new_pass="111111"):
        admin_pass = self.login.data_run(data("admin_pass"))
        login(self.driver, user_pass=lod_pass)
        self.login.change_pass()
        self.login.input_lod_pass(lod_pass)
        self.login.input_new_pass(new_pass)
        self.login.input_confirm_pass(new_pass)
        self.login.click_confirm_change()
        teardown(self.driver)
        print("【恢复密码】", self.login.data_run(data("admin_pass")) != admin_pass)
        os.system("allure generate ../../logs_file -o ../../logs_file/html")


if __name__ == '__main__':
    pytest.main(["-s", "test999_restore_pass.py"])



