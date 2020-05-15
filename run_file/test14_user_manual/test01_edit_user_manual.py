import pytest

from conf_file import user_manual
from base_file.base_yaml import data_yaml
from base_file.base_driver import setup, login


def data(key):
    return data_yaml("data_user_manual")[key]


class TestEditUserManual:

    def setup_class(self):
        self.driver = setup()
        self.manual = user_manual.UserManual(self.driver)
        login(self.driver)
        self.manual.open_user_manual()

    def teardown_class(self):
        self.driver.quit()

    # 编辑
    def test_edit_user_manual(self):
        self.manual.click_select_user_manual()
        self.manual.click_edit_user_manual()
        self.manual.input_edit_title(data("edit_title"))
        self.manual.select_manual(data("edit_file_name"))
        self.manual.click_edit_confirm()
        self.manual.text_element(user_manual.loc("title_text"), data("edit_title"), "【编辑用户手册】")


if __name__ == '__main__':
    pytest.main(["-s","test01_edit_user_manual.py"])