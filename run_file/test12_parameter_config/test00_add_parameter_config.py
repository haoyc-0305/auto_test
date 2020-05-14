import os, sys
sys.path.append(os.getcwd())
import pytest
from base_file.base_driver import setup, login
from conf_file import parameter_config
from base_file.base_yaml import data_yaml
from time import sleep


def data(key):
    return data_yaml("data_parameter_config")[key]


class TestAddParameterConfig:

    def setup_class(self):
        self.driver = setup()
        self.parameter = parameter_config.ParameterConfig(self.driver)
        login(self.driver)
        self.parameter.open_parameter_config()

    def teardown_class(self):
        self.driver.quit()

    # 创建软件存储
    @pytest.mark.parametrize("memory_info", data("add_parameter_config"))
    def test_add_parameter_config(self, memory_info):
        self.parameter.click_storage_config()
        self.parameter.click_select_software(memory_info["software_name"])
        self.parameter.click_add_storage()
        self.parameter.input_storage_info(memory_info["software_num"], memory_info["storage_server_ip"],
                                          memory_info["storage_server_path"], memory_info["memory_space"])
        self.parameter.click_save()
        self.parameter.element_number(parameter_config.loc("soft_info_loc"), int(memory_info["software_num"]) + 1,
                                      "软件存储【%s】" % memory_info["software_name"])


if __name__ == '__main__':
    pytest.main(["-s", "test00_add_parameter_config.py"])






