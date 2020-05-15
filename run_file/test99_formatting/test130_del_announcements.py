import pytest

from conf_file import announcements
from base_file.base_yaml import data_yaml
from base_file.base_driver import setup, login


def data(key):
    return data_yaml("data_announcements")[key]


class TestDelAnnouncements:

    def setup_class(self):
        self.driver = setup()
        self.annot = announcements.Announcements(self.driver)
        login(self.driver)
        self.annot.open_announcements()

    def teardown_class(self):
        self.driver.quit()

    # 删除
    def test_del_announcements(self):
        number = self.annot.get_text(announcements.loc("number"))
        self.annot.click_select_announcements()
        self.annot.click_del_title()
        self.annot.click_confirm_del()
        self.annot.not_text_element(announcements.loc("number"), number, "【删除通知公告】")


if __name__ == '__main__':
    pytest.main(["-s","test130_del_announcements.py"])