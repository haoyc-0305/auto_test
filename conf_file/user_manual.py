from selenium.webdriver.common.by import By
from base_file.base_method import Method
from base_file.base_yaml import data_yaml


def loc(key):
    return tuple(eval(data_yaml("loc_user_manual")[key]))


class UserManual(Method):

    def __init__(self, driver):
        Method.__init__(self, driver)
        self.driver = driver

    # 打开用户手册
    def open_user_manual(self):
        self.click_element(loc("system_config"))
        self.click_element(loc("user_manual"))

    # 新建公告
    def click_add_user_manual(self):
        self.click_element(loc("add_user_manual"))

    # 标题
    def input_title(self, title):
        self.input_text(loc("title"), title)

    # 选择手册
    def select_manual(self, file_name):
        self.click_element(loc("select_file"))
        self.file_upload(file_name, wait=2)

    # 说明
    def input_declare(self, declare):
        self.input_text(loc("declare"), declare)

    # 新建确认
    def click_add_confirm(self):
        self.click_element(loc("add_confirm"))

    # 选中手册
    def click_select_user_manual(self):
        self.click_element(loc("select_user_manual"))

    # 编辑
    def click_edit_user_manual(self):
        self.click_element(loc("edit_user_manual"))

    # 编辑标题
    def input_edit_title(self, edit_title):
        self.input_text(loc("edit_title"), edit_title)

    # 编辑确定
    def click_edit_confirm(self):
        self.click_element(loc("edit_confirm"))

    # 删除
    def click_del_title(self):
        self.click_element(loc("del_title"))

    # 确认删除
    def click_confirm_del(self):
        self.click_element(loc("confirm_del"))