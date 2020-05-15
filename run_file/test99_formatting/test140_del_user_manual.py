import pytest

from conf_file import user_manual
from base_file.base_yaml import data_yaml
from base_file.base_driver import setup, login


def data(key):
    return data_yaml("data_user_manual")[key]


class TestDelUserManual:

    def setup_class(self):
        self.driver = setup()
        self.manual = user_manual.UserManual(self.driver)
        login(self.driver)
        self.manual.open_user_manual()

    def teardown_class(self):
        self.driver.quit()

    # 删除
    def test_del_manual(self):
        number = self.manual.get_text(user_manual.loc("number"))
        self.manual.click_select_user_manual()
        self.manual.click_del_title()
        self.manual.click_confirm_del()
        self.manual.not_text_element(user_manual.loc("number"), number, "【删除用户手册】")


if __name__ == '__main__':
    pytest.main(["-s","test130_del_manual.py"])