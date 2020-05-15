import pytest

from conf_file import announcements
from base_file.base_yaml import data_yaml
from base_file.base_driver import setup, login


def data(key):
    return data_yaml("data_announcements")[key]


class TestDetailsAnnouncements:

    def setup_class(self):
        self.driver = setup()
        self.annot = announcements.Announcements(self.driver)
        login(self.driver)
        self.annot.open_announcements()

    def teardown_class(self):
        self.driver.quit()

    # 详情
    def test_details_announcements(self):
        self.annot.click_details()
        self.annot.displayed_true(announcements.loc("details_loc"), "【打开公告详情】")


if __name__ == '__main__':
    pytest.main(["-s","test01_details_announcements.py"])