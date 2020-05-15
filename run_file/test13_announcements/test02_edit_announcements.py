import pytest

from conf_file import announcements
from base_file.base_yaml import data_yaml
from base_file.base_driver import setup, login


def data(key):
    return data_yaml("data_announcements")[key]


class TestEditAnnouncements:

    def setup_class(self):
        self.driver = setup()
        self.annot = announcements.Announcements(self.driver)
        login(self.driver)
        self.annot.open_announcements()

    def teardown_class(self):
        self.driver.quit()

    # 编辑
    def test_edit_announcements(self):
        self.annot.click_select_announcements()
        self.annot.click_edit_announcements()
        self.annot.input_edit_title(data("edit_announcements"))
        self.annot.click_confirm()
        self.annot.text_element(announcements.loc("title_text"), data("edit_announcements"), "【编辑通知公告】")


if __name__ == '__main__':
    pytest.main(["-s","test01_edit_user_manual.py"])