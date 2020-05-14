import re
from selenium.webdriver.common.by import By
from base_file.base_yaml import data_yaml
from base_file.base_method import Method


def loc(key):
    return tuple(eval(data_yaml("loc_parameter_config")[key]))


class ParameterConfig(Method):

    def __init__(self, driver):
        Method.__init__(self, driver)
        self.driver = driver

    # 打开参数配置
    def open_parameter_config(self):
        self.click_element(loc("system_config"))
        self.click_element(loc("parameter_config"))

    # 存储配置
    def click_storage_config(self):
        self.click_element(loc("storage_config"))

    # 选中软件
    def click_select_software(self, software):
        software_loc = str(loc("select_software")) % software
        self.click_element(tuple(eval(software_loc)), clear=0.5)

    # 添加
    def click_add_storage(self):
        self.click_element(loc("add_storage"))

    # 软件存储信息
    def input_storage_info(self, software_num, ip, path, memory):
        storage_ip = tuple(eval(str(loc("storage_ip")) % software_num))
        storage_path = tuple(eval(str(loc("storage_path")) % software_num))
        storage_protocol = tuple(eval(str(loc("storage_protocol")) % software_num))
        storage_protocol_nfs = tuple(eval(str(loc("storage_protocol_nfs")) % software_num))
        space = tuple(eval(str(loc("space")) % software_num))
        self.input_text(storage_ip, ip)
        self.input_text(storage_path, path)
        self.click_element(storage_protocol)
        self.click_element(storage_protocol_nfs)
        self.input_text(space, memory)

    # 保存
    def click_save(self):
        self.click_element(loc("save"))

    # 删除按钮
    def click_delete_software(self):
        self.click_element(loc("del_button"))