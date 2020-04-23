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

    # 新建软件
    @pytest.mark.parametrize("param", data("soft_parameters"))
    def test_new_software(self, param):
        soft_number = self.soft.get_text(software_manage.loc("soft_number"))
        self.soft.click_new_soft()
        self.soft.input_new_soft_name(param["soft_name"])
        self.soft.input_new_soft_version(param["soft_version"])
        self.soft.click_new_soft_classify(param["soft_classify"])
        self.soft.click_soft_system(param["system_class"])
        self.soft.click_new_soft_license(param["soft_license"])
        self.soft.click_new_soft_load(param["load_class"])
        self.soft.click_new_soft_connection(param["soft_connection"])
        self.soft.click_new_soft_upload_icon(param["soft_name"])
        self.soft.click_list_icon(param["soft_name"])
        self.soft.click_new_soft_admin()
        self.soft.input_new_soft_directory(param["soft_directory"])
        self.soft.input_new_soft_command(param["soft_command"])
        self.soft.input_new_soft_firm(param["soft_name"])
        self.soft.click_new_soft_time()
        self.soft.click_new_soft_units()
        self.soft.input_new_asset_num(param["asset_num"])
        self.soft.click_confrim()
        self.soft.not_text_element(software_manage.loc("soft_number"), soft_number, "新建软件【%s】" % param["soft_name"])


if __name__ == '__main__':
    pytest.main(["-s", "test00_new_software.py"])