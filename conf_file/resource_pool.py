from base_file.base_method import Method
from base_file.base_yaml import data_yaml
from selenium.webdriver.common.by import By


def loc(key):
    return tuple(eval(data_yaml("loc_resource_pool")[key]))


class ResourcePool(Method):

    def __init__(self, driver):
        Method.__init__(self, driver)
        self.driver = driver

    # 打开资源池管理
    def open_resource_pool(self):
        self.click_element(loc("resource_manage"))
        self.click_element(loc("resource_pool_manage"))

    # 新建资源池
    def click_new_resource_poll(self):
        self.click_element(loc("new_resource_pool"))

    # 组名
    def input_group_name(self, group_name):
        self.input_text(loc("group_name"), group_name)

    # 类型
    def click_type(self, type):
        self.click_element(loc("type"))
        if "image-vm" in type:
            self.click_element(loc("image_node_vm"))
        elif "image-entity" in type:
            self.click_element(loc("image_node_entity"))
        elif "compute-vm" in type:
            self.click_element(loc("compute_node_vm"))
        elif "compute-entity" in type:
            self.click_element(loc("compute_node_entity"))

    # 应用软件
    def click_soft(self, soft_name):
        self.click_element(loc("soft"))
        if "cgg" in soft_name:
            self.click_element(loc("soft_cgg"))
        elif "landmark" in soft_name:
            self.click_element(loc("soft_landmark"))
        elif "omega" in soft_name:
            self.click_element(loc("soft_omega"))
        elif "petrel" in soft_name:
            self.click_element(loc("soft_petrel"))
        elif "mtsoft2d" in soft_name:
            self.click_element(loc("soft_mtsoft2d"))

    # 描述
    def input_describe(self, describe):
        self.input_text(loc("describe"), describe)

    # 新建搜索
    def input_search(self, search_text):
        self.input_text(loc("input_search"), search_text)
        self.click_element(loc("click_search"), clear=0.5)

    # 选中节点
    def click_node(self):
        self.click_element(loc("select"))

    # 新建确认
    def click_new_confirm(self):
        self.click_element(loc("new_confirm"))

    # 点击资源池
    def click_resource_pool(self):
        self.click_element(loc("click_resource"))

    # 编辑备注
    def input_edit_resource(self, edit_resource):
        self.input_text(loc("edit_describe"), edit_resource)

    # 下载模版文件
    def click_download_file(self):
        self.click_element(loc("download_file"))

    # 导入
    def click_upload_file(self):
        self.click_element(loc("upload_file"))

    # 导出
    def click_export_file(self):
        self.click_element(loc("export_file"))

    # 搜索
    def input_search_input(self, text):
        self.input_text(loc("search_input"), text)
        self.click_element(loc("search_button"))

    # 详情
    def click_particulars(self):
        self.click_element(loc("particulars"))

    # 选中所有资源池
    def click_select_all(self):
        self.click_element(loc("select_all"))

    # 点击删除按钮
    def click_delete_button(self):
        self.click_element(loc("delete_button"))

    # 确认删除
    def click_delete_confirm(self):
        self.click_element(loc("delete_confirm"))
