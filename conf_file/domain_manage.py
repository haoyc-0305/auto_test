from base_file.base_method import Method
from selenium.webdriver.common.by import By
from base_file.base_yaml import data_yaml


def loc(key):
    return tuple(eval(data_yaml("loc_domain")[key]))


class DomainManage(Method):

    def __init__(self, driver):
        Method.__init__(self, driver)
        self.driver = driver

    # 打开域管理
    def open_domain(self):
        self.click_element(loc("organization_manage"))
        self.click_element(loc("domain_manage"))

    # 创建域
    def click_new_domain(self):
        self.click_element(loc("domain_new"))

    # 输入域名
    def input_domain_name(self, domain_name):
        self.input_text(loc("domain_name"), domain_name)

    # 域类型下拉框
    def click_domain_class(self):
        self.click_element(loc("domain_class"))

    # 选中AD
    def click_domain_ad(self):
        self.click_element(loc("domain_ad"), clear=1)

    # 选中NIS
    def click_domain_nis(self):
        self.click_element(loc("domain_nis"), clear=1)

    # 输入主域IP
    def input_domain_master_ip(self, master_ip):
        self.input_text(loc("domain_master_ip"), master_ip)

    # 输入从域IP
    def input_domain_slave_ip(self, slave_ip):
        self.input_text(loc("domain_slave_ip"), slave_ip)

    # 输入用户名
    def input_domain_user(self, user_name):
        self.input_text(loc("system_name"), user_name)

    # 输入密码
    def input_domain_pass(self, user_pass):
        self.input_text(loc("system_pass"), user_pass)

    # 输入描述信息
    def input_domain_describe(self, user_describe):
        self.input_text(loc("domain_describe"), user_describe)

    # 确定创建
    def click_new_confirm(self):
        self.click_element(loc("domain_confirm"))

    # 编辑域
    def click_check_domain(self):
        self.click_element(loc("domain_ad_loc"))

    # 编辑域描述
    def input_describe(self, describe, clear=None):
        self.input_text(loc("input_describe"), describe, clear)

    # 确定编辑
    def click_edit_confirm(self):
        self.click_element(loc("domain_edit_confirm"))

    # 点击新建域用户
    def click_new_domain_user(self):
        self.click_element(loc("system_user_new"))

    # 输入域用户名
    def input_system_user_name(self, user_name):
        self.input_text(loc("system_user_name"), user_name)

    # 输入域用户密码
    def input_system_user_pass(self, user_pass):
        self.input_text(loc("system_user_pass0"), user_pass)

    # 输入域用户ID
    def input_system_user_id(self, user_id):
        self.input_text(loc("system_user_id"), user_id)

    # 输入域用户组ID
    def input_system_user_group_id(self, user_group_id):
        self.input_text(loc("system_user_group_id"), user_group_id)

    # 输入域用户目录
    def input_system_user_home(self, user_home):
        self.input_text(loc("system_user_home"), user_home)

    # 输入域用户备注
    def input_system_user_describe(self, user_describe):
        self.input_text(loc("system_user_describe"), user_describe)

    # 确认创建
    def click_system_user_confirm(self):
        self.click_element(loc("system_user_confirm"))

    # 同步用户
    def click_loading_user(self):
        self.click_element(loc("loading_user"))

    # 下载模板文件
    def download_file(self):
        self.click_element(loc("download_file"))

    # 导入
    def upload_file(self):
        self.click_element(loc("upload_file"))

    # 选中移除用户
    def click_select_user(self):
        self.click_element(loc("remove_select_user"))

    # 点击移除
    def click_remove_user(self):
        self.click_element(loc("remove_user"))

    # 点击还原
    def click_reduction_user(self):
        self.click_element(loc("reduction_user"))

    # 选中还原用户
    def click_reduction_select(self):
        self.click_element(loc("reduction_select"))

    # 确定还原
    def click_reduction_confirm(self):
        self.click_element(loc("restore_confirm"))

    # 导出域用户
    def click_export_user(self):
        self.click_element(loc("export_user"))

    # 输入搜索用户
    def find_system_user(self, system_user):
        self.input_text(loc("find_input_user"), system_user)

    # 点击搜索按钮
    def click_find(self):
        self.click_element(loc("find_click"))

    # 点击修改密码按钮
    def click_edit_pass(self):
        self.click_element(loc("edit_pass"))

    # 输入密码一
    def input_pass0(self, user_pass):
        self.input_text(loc("input_pass0"), user_pass)

    # 输入密码二
    def input_pass1(self, user_pass):
        self.input_text(loc("input_pass1"), user_pass)

    # 确定修改密码
    def confirm_pass(self):
        self.click_element(loc("confirm_pass"))

    # 删除域用户
    def click_delete_user(self):
        self.click_element(loc("delete_user"))

    def click_confirm(self):
        self.click_element(loc("confirm"))

    # 选中所有域
    def click_all_domain(self):
        self.click_element(loc("select_all_domain"), clear=1)

    # 删除域按钮
    def click_delete_domain(self):
        self.click_element(loc("domain_delete"))