import os, sys
sys.path.append(os.getcwd())
import pytest
from base_file.base_driver import setup, login, teardown
from conf_file import login_page
from time import sleep


class TestLogin:

    def setup(self):
        self.driver = setup()
        self.login = login_page.LoginPage(self.driver)

    def teardown(self):
        self.driver.quit()

    def test_change_pass(self, lod_pass="111111", new_pass="222222", text="用户登录", change_pass="【修改密码】"):
        login(self.driver)
        self.login.change_pass()
        self.login.input_lod_pass(lod_pass)
        self.login.input_new_pass(new_pass)
        self.login.input_confirm_pass(new_pass)
        self.login.click_confirm_change()
        teardown(self.driver)
        login(self.driver)
        self.login.out_verify(text, change_pass)

    def test_restore_pass(self, lod_pass="222222", new_pass="111111", text="用户登录", change_pass="【恢复密码】"):
        login(self.driver, user_pass=lod_pass)
        self.login.change_pass()
        self.login.input_lod_pass(lod_pass)
        self.login.input_new_pass(new_pass)
        self.login.input_confirm_pass(new_pass)
        self.login.click_confirm_change()
        teardown(self.driver)
        login(self.driver, user_pass=lod_pass)
        self.login.out_verify(text, change_pass)


if __name__ == '__main__':
    pytest.main(["-s", "test999_restore_pass.py"])



