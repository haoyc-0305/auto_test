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

    # 删除基本信息
    @pytest.mark.parametrize("del_info", data("del_info"))
    def test_delete_basic_info(self, del_info):
        info_num = self.info.get_element_num(basic_info.loc("checout"))
        info = str(basic_info.loc("del_element")) % del_info["info_name"]
        loc_info = tuple(eval(info))
        self.info.click_element(loc_info)
        self.info.delete()
        self.info.not_element_number(basic_info.loc("checout"), info_num, "删除【%s】" % del_info["info_name"])


if __name__ == '__main__':
    pytest.main(["-s", "test110_delete_basic_info.py"])




