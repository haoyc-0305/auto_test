from base_file.base_method import Method
from selenium.webdriver.common.by import By
from base_file.base_yaml import data_yaml


def loc(key):
    return tuple(eval(data_yaml("loc_hardware")[key]))


class HardwareManage(Method):

    def __init__(self, driver):
        Method.__init__(self, driver)
        self.driver = driver

    # 打开硬件资源管理
    def open_hardware_manage(self):
        self.click_element(loc("resource_manage"))
        self.click_element(loc("hardware_manage"))

    # 新建设备
    def click_new_hardware(self):
        self.click_element(loc("new_hardware"))

    # 打开系统类型
    def click_system_type(self):
        self.click_element(loc("system_type"))

    # 系统类型
    def click_system_types(self, type):
        if type == "linux":
            self.click_element(loc("system_linux"))
        elif type == "windows":
            self.click_element(loc("system_windows"))
        elif type == "windows_server":
            self.click_element(loc("system_windows_server"))

    # 设备类型
    def click_type(self):
        self.click_element(loc("type"))

    # 图形节点/虚机
    def click_types(self, type):
        if "gui_vm" in type:
            self.click_element(loc("gui_vm"))
        elif "calculate_vm" in type:
            self.click_element(loc("calculate_vm"))
        elif "gui_entity" in type:
            self.click_element(loc("gui_entity"))
        elif "calculate_entity" in type:
            self.click_element(loc("calculate_entity"))

    # IP(外网)
    def input_out_ip(self, out_ip):
        self.input_text(loc("out_ip"), out_ip)

    # IP(外网)
    def input_in_ip(self, in_ip):
        self.input_text(loc("in_ip"), in_ip)

    # 描述
    def input_describe(self, describe):
        self.input_text(loc("describe"), describe)

    # 品牌
    def click_brand(self):
        self.click_element(loc("brand"))

    # 品牌-华为
    def click_brands(self, brand):
        if brand == "华为":
            self.click_element(loc("huawei"))
        elif brand == "联想":
            self.click_element(loc("lenovo"))

    # 型号
    def input_model(self, model):
        self.input_text(loc("model"), model)

    # 序号
    def input_sn(self, sn):
        self.input_text(loc("sn"), sn)

    # 购买时间
    def click_time(self):
        self.click_element(loc("time"))

    # 购买时间-此刻
    def click_now(self):
        self.click_element(loc("now"))

    # 资产编号
    def input_asset_num(self, asset_num):
        self.input_text(loc("asset_num"), asset_num)

    # 保修期
    def click_warranty_time(self):
        self.click_element(loc("warranty_time"))

    # 保修期-两年
    def click_two_years_warranty(self):
        self.click_element(loc("two_years_warranty"))

    # 产权单位
    def click_subordinate_units(self):
        self.click_element(loc("subordinate_units"))

    # 产权单位-局级
    def click_unit_juji(self):
        self.click_element(loc("unit_juji"))

    # 关闭产权单位列表
    def click_shutdown_unit_list(self):
        self.click_element(loc("shutdown_unit_list"))

    # 设备管理员
    def click_device_manager(self):
        self.click_element(loc("device_manager"))

    # 设备管理员-haoyc00
    def click_device_admin(self):
        self.click_element(loc("device_haoyc00"))

    # 确定创建
    def click_confirm(self):
        self.click_element(loc("confrim"))

    # 编辑硬件
    def click_edit_hardware(self):
        self.click_element(loc("edit_hardware"))

    # 选中所有设备
    def click_select_all(self):
        self.click_element(loc("select_all"))

    # 更新设备
    def click_update_hardware(self):
        self.click_element(loc("update_hardware"))

    # 确认更新
    def click_update_confirm(self):
        self.click_element(loc("update_confirm"))

    # 下载模版文件
    def click_download_file(self):
        self.click_element(loc("download_file"))

    # 导入
    def click_upload_file(self):
        self.click_element(loc("upload_file"))

    # 导出
    def click_export_file(self):
        self.click_element(loc("export_file"))

    # 搜索
    def input_search_input(self, text):
        self.input_text(loc("search_input"), text)
        self.click_element(loc("search_button"))

    # 停用
    def click_block_up(self):
        self.click_element(loc("block_up"))

    # 启用
    def click_start(self):
        self.click_element(loc("start"))

    # 删除
    def click_delete(self):
        self.click_element(loc("delete"))