from time import sleep
from selenium.webdriver.common.by import By
from base_file.base_yaml import data_yaml
from base_file.base_method import Method


def loc(key):
    return tuple(eval(data_yaml("loc_basic_info")[key]))


class BasicInfo(Method):

    def __init__(self, driver):
        Method.__init__(self, driver)
        self.driver = driver

    # 打开基本信息
    def open_basic_info(self):
        self.click_element(loc("system_config"))
        self.click_element(loc("basic_info"))

    # 新增
    def add_info(self):
        self.click_element(loc("add_info"))

    # 类型
    def type(self, subtype):
        self.click_element(loc("type"))
        sleep(0.5)
        if "域" in subtype:
            self.click_element(loc("type_domain"))
        elif "连接" in subtype:
            self.click_element(loc("type_connect"))
        elif "负载均衡" in subtype:
            self.click_element(loc("type_load"))
        elif "职位" in subtype:
            self.click_element(loc("type_post"))
        elif "硬件" in subtype:
            self.click_element(loc("type_hardware"))
        elif "软件" in subtype:
            self.click_element(loc("type_software"))
        elif "操作系统" in subtype:
            self.click_element(loc("type_os"))

    # 子类
    def subtype(self, subtype):
        self.click_element(loc("subtype"))
        if "域类型" in subtype:
            self.click_element(loc("domain_type"))
        elif "连接方式" in subtype:
            self.click_element(loc("connect_way"))
        elif "负载均衡" in subtype:
            self.click_element(loc("load_leveling"))
        elif "职位名称" in subtype:
            self.click_element(loc("post_name"))
        elif "品牌" in subtype:
            self.click_element(loc("hardware_brand"))
        elif "资源类型" in subtype:
            self.click_element(loc("hardware_resource_type"))
        elif "软件类型" in subtype:
            self.click_element(loc("software_type"))
        elif "许可分类" in subtype:
            self.click_element(loc("software_license_type"))
        elif "软件图标" in subtype:
            self.click_element(loc("software_icon"))
        elif "操作系统" in subtype:
            self.click_element(loc("sub_os"))

    # 信息名称
    def input_info_name(self, info_name, icon_name=None, sn=None):
        if "职位名称" in info_name:
            self.input_text(loc("post_sn"), sn)
            self.input_text(loc("add_info_name"), info_name)
        elif "软件图标" in info_name:
            self.input_text(loc("icon_name"), info_name)
            self.click_element(loc("select_icon"))
            self.file_upload(icon_name)
        else:
            self.input_text(loc("add_info_name"), info_name)

    # 确定
    def add_confirm(self):
        self.click_element(loc("add_confirm"))
        sleep(2)

    # 删除
    def delete(self):
        self.click_element(loc("del_info"))

