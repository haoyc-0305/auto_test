import os, sys
sys.path.append(os.getcwd())
import pytest
from base_file.base_driver import setup, login
from conf_file import parameter_config
from base_file.base_yaml import data_yaml


def data(key):
    return data_yaml("data_parameter_config")[key]


class TestDelParameterConfig:

    def setup_class(self):
        self.driver = setup()
        self.parameter = parameter_config.ParameterConfig(self.driver)
        login(self.driver)
        self.parameter.open_parameter_config()

    def teardown_class(self):
        self.driver.quit()

    # 创建软件存储
    def test_del_parameter_config(self):
        loc_number = self.parameter.get_element_num(parameter_config.loc("software_number"))
        number = 0
        while number < loc_number:
            self.parameter.click_delete_software()
            self.parameter.click_save()
            self.parameter.not_element_number(parameter_config.loc("software_number"), loc_number, "【删除软件存储】")
            number += 1


if __name__ == '__main__':
    pytest.main(["-s", "test120_del_parameter_config.py"])






