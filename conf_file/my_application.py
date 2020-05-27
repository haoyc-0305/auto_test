from time import sleep
from selenium.webdriver.common.by import By
from base_file.base_method import Method
from base_file.base_yaml import data_yaml


def loc(key):
    return tuple(eval(data_yaml("loc_my_application")[key]))


class MyApplication(Method):

    def __init__(self, driver):
        Method.__init__(self, driver)
        self.driver = driver

    # 打开软件
    def open_application(self, soft_num):
        open_loc = str(loc("open_app")) % soft_num
        self.click_element(tuple(eval(open_loc)))
        sleep(5)

    # 获取软件名称元素
    def loc_soft(self, soft_num):
        soft_loc = str(loc("soft_name")) % soft_num
        soft_name = self.get_text(tuple(eval(soft_loc)))
        return soft_name


    # 搜索
    def search_connection(self, soft_name):
        self.input_text(loc("search_input"), soft_name)
        self.click_element(loc("search_button"))

    # 详情
    def click_details(self):
        self.click_element(loc("details"))

    # 关闭
    def click_close(self):
        self.click_element(loc("close"))
        self.click_element(loc("close_confirm"))

    # 培训资料
    def click_cultivate_material(self):
        self.click_element(loc("cultivate_material"))

    # 预览
    def click_preview(self):
        self.click_element(loc("preview"))
        sleep(5)

    # 下载
    def click_download(self):
        self.click_element(loc("download"))

    # 留言
    def click_leave_word(self, text):
        self.click_element(loc("leave_word"))
        self.input_text(loc("input_leave_word"), text)
        self.click_element(loc("publish"))

    # 我的分享
    def click_my_share(self):
        self.click_element(loc("my_share"))

    # 我的分享-关闭
    def click_my_share_close(self):
        self.click_element(loc("my_share_close"))
        self.click_element(loc("my_share_close_confirm"))

    # 我的分享-共享
    def click_share(self):
        self.click_element(loc("share"))

    # 我的共享-选择用户
    def click_share_department(self):
        self.click_element(loc("share_department"))
        self.click_element(loc("share_user"))
        self.click_element(loc("share_move_user"))
        self.click_element(loc("share_confirm"))

    # 清空分享
    def click_clear_share(self):
        self.click_element(loc("clear_share"))

    # 我的连接全选
    def click_select_all_connection(self):
        self.click_element(loc("select_all_connection"))

    # 批量关闭
    def click_batch_close(self):
        self.click_element(loc("batch_close"))
        self.click_element(loc("batch_close_confirm"))
        sleep(5)