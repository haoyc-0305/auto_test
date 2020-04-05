from selenium.webdriver.common.by import By
from base_file.base_method import Method
from base_file.base_yaml import data_yaml


def loc(key):
    return tuple(eval(data_yaml("loc_authority")[key]))


class AuthorityManage(Method):

    def __init__(self, driver):
        Method.__init__(self, driver)
        self.driver = driver

    # 打开职权管理
    def open_authority(self):
        self.click_element(loc("organization_manage"))
        self.click_element(loc("authority_manage"))

    # 新建职权按钮
    def click_authority_create(self):
        self.click_element(loc("authority_create"))

    # 职权名称输入框
    def input_authority_name(self, authority_name):
        self.input_text(loc("authority_input_name"), authority_name)

    # 确定创建按钮
    def click_confirm_authority(self):
        self.click_element(loc("authority_confirm"))

    # 选择测试职权
    def click_test_authority_name(self, clear=None):
        self.click_element(loc("test_authority_name"), clear)

    # 选中应用管理员
    def click_app_authority_name(self, clear=None):
        self.click_element(loc("app_authority_name"), clear)

    # 选中设备管理员
    def click_device_authority_name(self, clear=None):
        self.click_element(loc("device_authority_name"), clear)

    # 选中系统管理员
    def click_system_authority_name(self, clear=None):
        self.click_element(loc("system_authority_name"), clear)


    # 选择权限
    def click_powers_all(self):
        self.click_element(loc("powers_all"))

    # 确定权限
    def click_powers_confirm(self):
        self.click_element(loc("powers_confirm"))

    # 添加职权用户按钮
    def click_authority_add_user(self):
        self.click_element(loc("authority_add_user"))

    # 选中职权用户
    def click_authority_user_name(self):
        self.click_element(loc("rank_select"))

    # 确定添加职权用户
    def click_confirm_select(self):
        self.click_element(loc("authority_confirm"))

    # 选择职权
    def click_authority_del_select(self):
        self.click_element(loc("authority_add_name"))

    # 选择移除用户
    def click_authority_del_user_select(self):
        self.click_element(loc("authority_del_user_select"))

    # 确认移除
    def click_authority_del_user_confirm(self):
        self.click_element(loc("authority_del_user_confirm"))

    # 删除职权
    def click_authority_del(self):
        self.click_element(loc("authority_del"))

    # 确认删除职权
    def click_authority_del_confirm(self):
        self.click_element(loc("authority_del_confirm"))

