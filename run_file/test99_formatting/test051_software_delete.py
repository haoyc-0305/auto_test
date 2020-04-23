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

    # 删除软件
    def test_software_delete(self):
        soft_number = self.soft.get_text(software_manage.loc("soft_number"))
        self.soft.click_software_all()
        self.soft.click_delete()
        self.soft.click_software_delete_confirm()
        self.soft.not_text_element(software_manage.loc("soft_number"), soft_number, "【软件删除】")


if __name__ == '__main__':
    pytest.main(["-s", "test051_software_delete.py"])