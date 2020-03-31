from selenium.webdriver.common.by import By

from base_file.base_yaml import data_yaml
from base_file.base_method import Method


def loc(key):
    return tuple(eval(data_yaml("loc_user_manage")[key]))


class UserManage(Method):

    def __init__(self, driver):
        Method.__init__(self, driver)
        self.driver = driver

    # 打开用户管理
    def open_user_manage(self):
        self.click_element(loc("organization_manage"))
        self.click_element(loc("user_manage"))

    # 打开编辑职级
    def click_edit_rank(self, clrar=None):
        self.click_element(loc("edit_rank_loc"), clrar)

    # 创建下级职级
    def click_rank_lower(self):
        self.click_element(loc("edit_rank_lower"))

    # 输入职级名称
    def input_rank_name(self, rank_name):
        self.input_text(loc("edit_input_rank_name"), rank_name)

    # 确认创建
    def click_edit_rank_confirm(self):
        self.click_element(loc("edit_rank_confirm"))

    # 选中职级
    def click_lower_rank(self):
        self.click_element(loc("edit_rank_name"))

    # 确认删除
    def click_delete_rank(self):
        self.click_element(loc("edit_rank_delete"))

    # 创建组织
    def click_create_department(self):
        self.click_element(loc("department_create"))

    # 输入部门名称
    def input_department_name(self, department_name):
        self.input_text(loc("department_name"), department_name)

    # 行政级别
    def click_rank_list(self):
        self.click_element(loc("rank_list"))

    # 局级单位
    def click_rank_juji(self, clear=None):
        self.click_element(loc("rank_juji"), clear)

    # 处级单位
    def click_rank_chuji(self, clear=None):
        self.click_element(loc("rank_chuji"), clear)

    # 科级单位
    def click_rank_keji(self, clear=None):
        self.click_element(loc("rank_keji"), clear)

    # 邮箱输入
    def input_email(self, email):
        self.input_text(loc("email"), email)

    # 主管单位
    def click_director(self):
        self.click_element(loc("director"))

    # 新建_局级主管
    def click_new_director_juji(self):
        self.click_element(loc("director_juji"))

    # 新建_处级主管
    def click_new_director_chuji(self):
        self.click_element(loc("director_chuji"))

    # 确认创建部门
    def click_department_confirm(self):
        self.click_element(loc("department_confirm"))

    # 编辑_选中局级
    def click_director_edit_juji(self):
        self.click_element(loc("department_rank_juji"))

    # 编辑_选中处级
    def click_director_edit_chuji(self):
        self.click_element(loc("department_rank_chuji"))

    # 编辑_选中科级
    def click_director_edit_keji(self):
        self.click_element(loc("department_rank_keji"))

    # 编辑部门按钮
    def click_edit_department(self):
        self.click_element(loc("department_edit"))

    # 编辑_局级主管
    def click_edit_director_juji(self):
        self.click_element(loc("edit_director_juji"))

    # 编辑_处级主管
    def click_edit_director_chuji(self):
        self.click_element(loc("edit_director_chuji"))

    # 删除部门按钮
    def click_delete_department(self):
        self.click_element(loc("delete_department"))

    # 删除_选中科级
    def click_edit_rank_keji(self):
        self.click_element(loc("edit_rank_keji"))

    # 删除_选中处级
    def click_edit_rank_chuji(self):
        self.click_element(loc("edit_rank_chuji"))

    # 删除_选中局级
    def click_edit_rank_juji(self):
        self.click_element(loc("edit_rank_juji"))

    # 删除_确认
    def click_delete_department_confirm(self):
        self.click_element(loc("delete_department_confirm"))

    # 新建用户按钮
    def click_user_create(self):
        self.click_element(loc("user_create"))

    # 用户名输入框
    def input_user_name(self, user_name):
        self.input_text(loc("user_name"), user_name)

    # 姓名输入框
    def input_name(self, name):
        self.input_text(loc("name"), name)

    # 单位列表
    def click_unit_list(self):
        self.click_element(loc("unit_list"))

    # 局级单位
    def click_unit_juji(self):
        self.click_element(loc("unit_ji"))

    # 处级单位
    def click_unit_chuji(self):
        self.click_element(loc("unit_chuji"))

    # 科级单位
    def click_unit_keji(self):
        self.click_element(loc("unit_keji"))

    # IP地址输入框
    def input_ip_address(self, ip):
        self.input_text(loc("ip_address"), ip)

    # MAC地址输入框
    def input_mac_address(self, mac):
        self.input_text(loc("mac_address"), mac)

    # 性别男
    def click_man(self):
        self.click_element(loc("man"))

    # 性别女
    def click_women(self):
        self.click_element(loc("women"))

    # 电话输入框
    def input_tel(self, tel):
        self.input_text(loc("tel"), tel)

    # 手机输入框
    def input_mobile(self, mobile):
        self.input_text(loc("mobile"), mobile)

    # AD域复选框
    def click_ad(self):
        self.click_element(loc("ad"))

    # NIS域复选框
    def click_nis(self):
        self.click_element(loc("nis"))

    # 确认创建用户
    def click_user_create_confirm(self):
        self.click_element(loc("user_create_confirm"))

    # 下载模板
    def click_download_template(self):
        self.click_element(loc("download_template"))

    # 导入按钮
    def click_import_template(self):
        self.click_element(loc("import_template"))

    # 用户全选
    def click_user_all(self):
        self.click_element(loc("user_all"))

    # 用户冻结
    def click_user_freeze(self):
        self.click_element(loc("freeze"))

    # 用户解锁
    def click_user_unlock(self):
        self.click_element(loc("unlock"))

    # 编辑用户
    def click_user_edit(self):
        self.click_element(loc("user_edit"))

    # 选中科级部门
    def click_select_keji(self):
        self.click_element(loc("select_keji"))

    # 用户搜索
    def input_user_find(self, user_name):
        self.input_text(loc("find_box"), user_name)
        self.click_element(loc("find_button"))

    # 修改密码按钮
    def click_change_pass(self):
        self.click_element(loc("change_pass"))

    # 输入新密码
    def input_new_pass(self, user_pass):
        self.input_text(loc("new_pass"), user_pass)

    # 确认密码
    def input_confirm_pass(self, user_pass):
        self.input_text(loc("confirm_pass"), user_pass)

    # 确认修改
    def click_change_pass_confirm(self):
        self.click_element(loc("change_pass_confirm"))

    # 用户导出
    def click_user_export(self):
        self.click_element(loc("user_export"))

    # 删除用户
    def click_user_delete(self):
        self.click_element(loc("user_delete"))

    # 删除云盘数据
    def click_cloud_data(self):
        self.click_element(loc("cloud_data_delete"))

    # 确认删除用户
    def click_user_delete_confirm(self):
        self.click_element(loc("user_delete_confirm"))
