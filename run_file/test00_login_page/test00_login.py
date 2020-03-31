import os, sys
sys.path.append(os.getcwd())
import pytest
from base_file.base_driver import setup, teardown
from conf_file import login_page


class TestLogin:

    def setup_class(self):
        self.driver = setup()
        self.login = login_page.LoginPage(self.driver)

    def teardown_class(self):
        teardown(self.driver)

    def test_login(self, user="admin", text_name="【用户登录】"):
        self.login.input_user("admin")
        self.login.input_pass("111111")
        self.login.click_login()
        self.login.login_verify(user, text_name)


if __name__ == '__main__':
    pytest.main(["-s", "test00_login.py"])



