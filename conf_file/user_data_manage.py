from time import sleep

from base_file.base_yaml import data_yaml
from base_file.base_method import Method
from selenium.webdriver.common.by import By


def loc(key):
    return tuple(eval(data_yaml("loc_user_data_manage")[key]))


class UserDataManage(Method):

    def __init__(self, driver):
        Method.__init__(self, driver)
        self.driver = driver

    # 打开用户数据管理
    def open_user_data_manage(self):
        self.click_element(loc("data_manage"))
        self.click_element(loc("user_data_manage"))

    # 选择软件存储
    def click_soft_store(self):
        self.click_element(loc("soft_store"))

    # 新建文件夹
    def click_new_folder(self):
        self.click_element(loc("new_folder"))

    # 文件夹名称
    def input_folder_name(self, folder_name):
        self.input_text(loc("folder_name"), folder_name)

    # 文件备注
    def input_folder_remark(self, folder_remark):
        self.input_text(loc("folder_remark"), folder_remark)

    # 确定新建
    def click_confirm_new_folder(self):
        self.click_element(loc("confirm_new_folder"))

    # 文件上传
    def click_file_upload(self, file_name):
        self.click_element(loc("upload"))
        self.click_element(loc("upload_button"))
        self.file_upload(file_name)
        self.click_element(loc("upload_confirm"), clear=1)
        self.click_element(loc("reconfirm"))

    # 选择文件
    def click_select_file(self):
        self.click_element(loc("select_file"))

    # 下载
    def click_download(self, name):
        self.click_element(loc("download"))
        self.file_find(name)

    # 复制到
    def click_copy(self):
        self.click_element(loc("copy_button"))
        self.click_element(loc("copy_select_folder"))
        self.click_element(loc("copy_confirm"))
        sleep(2)

    # 返回上级
    def click_return(self):
        self.click_element(loc("return"))

    # 移动到
    def click_move(self):
        self.click_element(loc("move_button"))
        self.click_element(loc("move_select_folder"))
        self.click_element(loc("move_confirm"))
        sleep(2)

    # 选择编辑文件夹
    def click_select_edit_folder(self):
        self.click_element(loc("select_edit_folder"))

    # 编辑按钮
    def click_edit_button(self):
        self.click_element(loc("edit_button"))

    # 编辑名称
    def input_edit_name(self, edit_name):
        self.input_text(loc("edit_name"), edit_name)

    # 编辑备注
    def input_edit_remark(self, edit_remark):
        self.input_text(loc("edit_remark"), edit_remark)

    # 确认编辑
    def click_confirm_edit_folder(self):
        self.click_element(loc("confirm_edit_folder"))
