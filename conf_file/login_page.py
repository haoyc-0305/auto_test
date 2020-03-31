from base_file.base_method import Method
from selenium.webdriver.common.by import By
from base_file.base_yaml import data_yaml


def loc(key):
    return tuple(eval(data_yaml("loc_login")[key]))


class LoginPage(Method):

    def __init__(self, driver):
        Method.__init__(self, driver)
        self.driver = driver

    # 输入用户名
    def input_user(self, user_name):
        self.input_text(loc("user_name"), user_name)

    # 输入密码
    def input_pass(self, password):
        self.input_text(loc("user_pass"), password)

    # 登陆
    def click_login(self):
        self.click_element(loc("user_login"))

    # 登陆校验
    def login_verify(self, text, text_name):
        self.text_element(loc("user_text"), text, text_name)

    # 点击修改密码按钮
    def change_pass(self):
        self.mouse_element(loc("user_text"))
        self.click_element(loc("change_pass"))

    # 输入旧密码
    def input_lod_pass(self, lod_pass):
        self.input_text(loc("lod_pass"), lod_pass)

    # 输入新密码
    def input_new_pass(self, new_pass):
        self.input_text(loc("new_pass"), new_pass)

    # 输入确认密码
    def input_confirm_pass(self, confirm_pass):
        self.input_text(loc("confirm_pass"), confirm_pass)

    # 确认修改
    def click_confirm_change(self):
        self.click_element(loc("confirm_change"))

    # 注销校验
    def out_verify(self, text, text_name):
        self.text_element(loc("user_login_false"), text, text_name)

