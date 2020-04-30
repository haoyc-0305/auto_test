from base_file.base_method import Method
from base_file.base_yaml import data_yaml
from selenium.webdriver.common.by import By


def loc(key):
    return tuple(eval(data_yaml("loc_resource_auth")[key]))


class ResourceAuth(Method):

    def __init__(self, driver):
        Method.__init__(self, driver)
        self.driver = driver

    # 打开资源授权
    def open_resource_auth(self):
        self.click_element(loc("resource_manage"))
        self.click_element(loc("open_resource_auth"))

    # 新建
    def click_new_resource_auth(self):
        self.click_element(loc("new_resource_auth"))

    # 选中用户
    def click_select_user(self):
        self.click_element(loc("select_user"))

    # 搜索软件
    def input_new_search_input(self, search):
        self.input_text(loc("new_search_input"), search)
        self.click_element(loc("new_search_button"))

    # 选中软件
    def click_select_soft(self):
        self.click_element(loc("select_soft"))

    # 选中资源组
    def click_select_resource_group(self):
        self.click_element(loc("select_resource_group"))

    # 完成创建
    def click_resource_auth_confirm(self):
        self.click_element(loc("resource_auth_confirm"))

    # 搜索资源授权
    def input_search_input(self, search_text):
        self.input_text(loc("search_input"), search_text)
        self.click_element(loc("search_button"))

    # 选中编辑授权
    def click_select_auth(self):
        self.click_element(loc("select_auth"))

    # 编辑
    def click_edit_resource(self):
        self.click_element(loc("edit_button"))

    # 编辑修改资源组
    def click_edit_select_resource_group(self):
        self.click_element(loc("edit_select_resource_group"))

    # 下载模版文件
    def click_download_file(self):
        self.click_element(loc("download_file"))

    # 导入
    def click_upload_file(self):
        self.click_element(loc("upload_file"))

    # 导出
    def click_export_file(self):
        self.click_element(loc("export_file"))

    # 删除
    def click_delete(self):
        self.click_element(loc("delete"))

    # 确认删除
    def click_delete_confirm(self):
        self.click_element(loc("delete_confirm"))