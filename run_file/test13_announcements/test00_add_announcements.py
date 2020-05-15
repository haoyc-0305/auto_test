import pytest

from conf_file import announcements
from base_file.base_yaml import data_yaml
from base_file.base_driver import setup, login


def data(key):
    return data_yaml("data_announcements")[key]


class TestAddAnnouncements:

    def setup_class(self):
        self.driver = setup()
        self.annot = announcements.Announcements(self.driver)
        login(self.driver)
        self.annot.open_announcements()

    def teardown_class(self):
        self.driver.quit()

    # 新建
    def test_add_announcements(self, add_info=data("add_announcements")):
        number = self.annot.get_text(announcements.loc("number"))
        self.annot.click_add_announcements()
        self.annot.click_log_show()
        self.annot.click_focus_show()
        self.annot.input_title(add_info["title"])
        self.annot.input_content(add_info["content"])
        self.annot.click_confirm()
        self.annot.not_text_element(announcements.loc("number"), number, "【新建通知公告】")


if __name__ == '__main__':
    pytest.main(["-s","test00_add_announcements.py"])