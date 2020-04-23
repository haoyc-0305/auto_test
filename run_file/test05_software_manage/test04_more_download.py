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

    # 更多功能_下载
    @pytest.mark.parametrize("more", data("more"))
    def test_more_download(self, more):
        self.soft.input_search_input(more["soft_name"])
        self.soft.click_more(more["loc"])
        self.soft.click_more_download()
        self.soft.file_find(more["upload_file"])
        self.driver.refresh()


if __name__ == '__main__':
    pytest.main(["-s", "test04_more_download.py"])