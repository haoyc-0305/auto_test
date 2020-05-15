import pytest
from conf_file import user_manual
from base_file.base_yaml import data_yaml
from base_file.base_driver import setup, login


def data(key):
    return data_yaml("data_user_manual")[key]


class TestAddUserManual:

    def setup_class(self):
        self.driver = setup()
        self.manual = user_manual.UserManual(self.driver)
        login(self.driver)
        self.manual.open_user_manual()

    def teardown_class(self):
        self.driver.quit()

    # 新建手册
    def test_add_user_manual(self):
        number = self.manual.get_text(user_manual.loc("number"))
        self.manual.click_add_user_manual()
        self.manual.input_title(data("add_title"))
        self.manual.select_manual(data("add_file_name"))
        self.manual.input_declare(data("add_declare"))
        self.manual.click_add_confirm()
        self.manual.not_text_element(user_manual.loc("number"), number, "【新建通知公告】")


if __name__ == '__main__':
    pytest.main(["-s","test00_add_user_manual.py"])