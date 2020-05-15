from selenium.webdriver.common.by import By
from base_file.base_method import Method
from base_file.base_yaml import data_yaml


def loc(key):
    return tuple(eval(data_yaml("loc_announcements")[key]))


class Announcements(Method):

    def __init__(self, driver):
        Method.__init__(self, driver)
        self.driver = driver

    # 打开通知公告
    def open_announcements(self):
        self.click_element(loc("system_config"))
        self.click_element(loc("announcements"))

    # 新建公告
    def click_add_announcements(self):
        self.click_element(loc("add_announcements"))

    # 登录页显示
    def click_log_show(self):
        self.click_element(loc("log_show"))

    # 着重显示
    def click_focus_show(self):
        self.click_element(loc("focus_show"))

    # 标题
    def input_title(self, title):
        self.input_text(loc("title"), title)

    # 内容
    def input_content(self, content):
        self.input_text(loc("content"), content)

    # 确定
    def click_confirm(self):
        self.click_element(loc("confirm"))

    # 详情
    def click_details(self):
        self.click_element(loc("details"))

    # 选中公告
    def click_select_announcements(self):
        self.click_element(loc("select_announcements"))

    # 编辑
    def click_edit_announcements(self):
        self.click_element(loc("edit_announcements"))

    # 编辑标题
    def input_edit_title(self, edit_title):
        self.input_text(loc("edit_title"), edit_title)

    # 删除
    def click_del_title(self):
        self.click_element(loc("del_title"))

    # 确认删除
    def click_confirm_del(self):
        self.click_element(loc("confirm_del"))