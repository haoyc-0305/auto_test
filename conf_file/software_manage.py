from base_file.base_method import Method
from selenium.webdriver.common.by import By
from base_file.base_yaml import data_yaml


def loc(key):
    return tuple(eval(data_yaml("loc_software")[key]))

class SoftwareManage(Method):
