from base_file.base_method import Method
from selenium.webdriver.common.by import By
from base_file.base_yaml import data_yaml


def loc(key):
    return tuple(eval(data_yaml("loc_software")[key]))


class SoftwareManage(Method):

    def __init__(self, driver):
        Method.__init__(self, driver)
        self.driver = driver

    # 打开软件资源管理
    def open_soft_manage(self):
        self.click_element(loc("resource_manage"))
        self.click_element(loc("hardware_manage"))

    # 新建软件
    def click_new_soft(self):
        self.click_element(loc("new_soft"))

    # 软件名称
    def input_new_soft_name(self, soft_name):
        self.input_text(loc("new_soft_name"), soft_name)

    # 软件版本
    def input_new_soft_version(self, soft_version):
        self.input_text(loc("new_soft_version"), soft_version)

    # 软件分类
    def click_new_soft_classify(self, soft_classify):
        self.click_element(loc("new_soft_classify"))
        if "dispose" in soft_classify:
            self.click_element(loc("soft_classify_dispose"))
        elif "count" in soft_classify:
            self.click_element(loc("soft_classify_count"))

    # 系统类型
    def click_soft_system(self, system_class):
        self.click_element(loc("new_soft_system"))
        if "win7" in system_class:
            self.click_element(loc("soft_system_win7"))
        elif "win10" in system_class:
            self.click_element(loc("soft_system_win10"))
        elif "redhat6" in system_class:
            self.click_element(loc("soft_system_redhat6"))
        elif "redhat7" in system_class:
            self.click_element(loc("soft_system_redhat7"))

    # 许可类型
    def click_new_soft_license(self, soft_license):
        self.click_element(loc("new_soft_license"))
        if "GeoEast" in soft_license:
            self.click_element(loc("soft_license_GeoEast"))
        elif "Flexlm" in soft_license:
            self.click_element(loc("soft_license_Flexlm"))

    # 负载类型
    def click_new_soft_load(self, load_class):
        self.click_element(loc("new_soft_load"))
        if "memory" in load_class:
            self.click_element(loc("soft_load_memory"))
        elif "cpu" in load_class:
            self.click_element(loc("soft_load_cpu"))

    # 连接方式
    def click_new_soft_connection(self, connection_class):
        self.click_element(loc("new_soft_connection"))
        if "realnc" in connection_class:
            self.click_element(loc("soft_connection_realvnc"))
        elif "dcv2019" in connection_class:
            self.click_element(loc("soft_connection_dcv2019"))
        elif "dcv2017" in connection_class:
            self.click_element(loc("soft_connection_dcv2017"))
        elif "dcv2016" in connection_class:
            self.click_element(loc("soft_connection_dcv2016"))
        elif "rdsh" in connection_class:
            self.click_element(loc("soft_connection_rdsh"))
        elif "xenapp" in connection_class:
            self.click_element(loc("soft_connection_xenapp"))
        elif "horizon" in connection_class:
            self.click_element(loc("soft_connection_horizon"))

    # 上传图标
    def click_new_soft_upload_icon(self, icon_name):
        self.click_element(loc("new_soft_upload_icon"))
        self.input_text(loc("icon_name"), icon_name)
        self.click_element(loc("select_icon_file"))
        self.file_upload("%s.png" % icon_name)
        self.click_element(loc("add_icon_confirm"))

    # 图标下拉框
    def click_list_icon(self, icon_name):
        self.click_element(loc("list_icon"))
        if "CGG" in icon_name:
            self.click_element(loc("select_icon_CGG"))
        elif "LandMark" in icon_name:
            self.click_element(loc("select_icon_LandMark"))
        elif "Omega" in icon_name:
            self.click_element(loc("select_icon_Omega"))
        elif "Petrel" in icon_name:
            self.click_element(loc("select_icon_Petrel"))
        elif "Mtsoft2D" in icon_name:
            self.click_element(loc("select_icon_Mtsoft2D"))

    # 应用管理员
    def click_new_soft_admin(self):
        self.click_element(loc("new_soft_admin"))
        self.click_element(loc("soft_admin"))

    # 软件目录
    def input_new_soft_directory(self, soft_directory):
        self.input_text(loc("new_soft_directory"), soft_directory)

    # 启动命令
    def input_new_soft_command(self, soft_command):
        self.input_text(loc("new_soft_command"), soft_command)

    # 厂商
    def input_new_soft_firm(self, soft_firm):
        self.input_text(loc("new_soft_firm"), soft_firm)

    # 购买时间
    def click_new_soft_time(self):
        self.click_element(loc("new_soft_time"))
        self.click_element(loc("now"))

    # 产权单位
    def click_new_soft_units(self):
        self.click_element(loc("new_soft_units"))
        self.click_element(loc("unit_juji"))
        self.click_element(loc("shutdown_unit_list"))

    # 资产编号
    def input_new_asset_num(self, asset_num):
        self.input_text(loc("new_asset_num"), asset_num)

    # 确认创建
    def click_confrim(self):
        self.click_element(loc("confrim"))



