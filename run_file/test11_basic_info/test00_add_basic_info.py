import os, sys
sys.path.append(os.getcwd())
import pytest
from base_file.base_driver import setup, login
from conf_file import basic_info
from base_file.base_yaml import data_yaml


def data(key):
    return data_yaml("data_basic_info")[key]


class TestAddInfo:

    def setup_class(self):
        self.driver = setup()
        self.info = basic_info.BasicInfo(self.driver)
        login(self.driver)
        self.info.open_basic_info()

    def teardown_class(self):
        self.driver.quit()

    # 新增基本信息
    @pytest.mark.parametrize("add_info", data("add_info"))
    def test_add_basic_info(self, add_info):
        info_num = self.info.get_element_num(basic_info.loc("checout"))
        self.info.add_info()
        self.info.type(add_info["type"])
        self.info.subtype(add_info["subtype"])
        if "职位名称" in add_info["subtype"]:
            self.info.input_info_name(add_info["info_name"], sn=add_info["sn"])
        elif "软件图标" in add_info["subtype"]:
            self.info.input_info_name(add_info["info_name"], icon_name=add_info["icon_name"])
        else:
            self.info.input_info_name(add_info["info_name"])
        self.info.add_confirm()
        self.info.not_element_number(basic_info.loc("checout"), info_num, "新增【%s】" % add_info["subtype"])


if __name__ == '__main__':
    pytest.main(["-s", "test00_add_basic_info.py"])




