import os, sys
from time import sleep

sys.path.append(os.getcwd())
import pytest
from base_file.base_driver import setup, login
from base_file.base_yaml import data_yaml
from conf_file import software_manage


def data(key):
    return data_yaml("data_software")[key]


class TestHardware:

    # 打开软件资源管理
    def setup_class(self):
        self.driver = setup()
        self.soft = software_manage.SoftwareManage(self.driver)
        login(self.driver)
        self.soft.open_soft_manage()

    def teardown_class(self):
        self.driver.quit()

    # 保存备注信息
    @pytest.mark.parametrize("more", data("more"))
    def test_more_remark(self, more):
        self.soft.input_search_input(more["soft_name"])
        self.soft.click_more(more["loc"])
        self.soft.input_note(more["remark"])
        self.soft.displayed_true(software_manage.loc("remark_loc"), "%s【保存备注】" % more["loc"])
        self.driver.refresh()


if __name__ == '__main__':
    pytest.main(["-s", "test05_more_remark.py"])