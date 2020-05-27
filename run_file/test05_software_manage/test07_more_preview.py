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

    # 文件浏览
    @pytest.mark.parametrize("preview", data("preview"))
    def test_more_preview(self, preview):
        self.soft.input_search_input(preview["soft_name"])
        self.soft.click_more(preview["loc"])
        self.soft.click_preview()
        self.soft.displayed_true(software_manage.loc("preview_loc"), "%s【文件预览】" % preview["loc"])
        self.driver.refresh()


if __name__ == '__main__':
    pytest.main(["-s", "test07_more_preview.py"])