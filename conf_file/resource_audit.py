from time import sleep

from base_file.base_method import Method
from base_file.base_yaml import data_yaml
from selenium.webdriver.common.by import By


def loc(key):
    return tuple(eval(data_yaml("loc_resource_audit")[key]))


class ResourceAudit(Method):

    def __init__(self, driver):
        Method.__init__(self, driver)
        self.driver = driver

    # 打开资源审批模块
    def open_resource_application(self, module_type):
        self.click_element(loc("resource_audit"))
        if "资源申请" in module_type:
            self.resource_application()
        elif "审批管理" in module_type:
            self.examine_manage()

    # 打开资源申请
    def resource_application(self):
        self.click_element(loc("resource_application"))

    # 打开审批管理
    def examine_manage(self):
        self.click_element(loc("audit_manage"))

    # 审批配置
    def click_audit_config(self):
        self.click_element(loc("audit_config"))

    # 科室列表
    def click_department_list(self):
        self.click_element(loc("department_list"))

    # 选中部门
    def click_select_department(self):
        self.click_element(loc("select_department"))

    # 添加
    def click_add_department(self):
        self.click_element(loc("add_department"))

    # 一级审批
    def click_level_one_audit(self):
        self.click_element(loc("level_one_audit"))

    # 二级审批
    def click_level_two_audit(self):
        self.click_element(loc("level_two_audit"))

    # 局级
    def click_juji(self):
        self.click_element(loc("juji"))

    # 一级处级
    def click_level_one_chuji(self):
        self.click_element(loc("level_one_chuji"))

    # 二级处级
    def click_level_two_chuji(self):
        self.click_element(loc("level_two_chuji"))

    # 一级审批人
    def click_level_one_approver(self):
        self.click_element(loc("level_one_approver"))

    # 二级审批人
    def click_level_two_approver(self):
        self.click_element(loc("level_two_approver"))

    # 保存
    def click_save(self):
        self.click_element(loc("save"))
        sleep(5)

    # 点击新建
    def click_new_resource_application(self):
        self.click_element(loc("new_resource_application"))

    # 点击申请类别
    def click_application_class(self, application_class):
        if "个人" in application_class:
            self.click_element(loc("application_class_personal"))
        elif "组织" in application_class:
            self.click_element(loc("application_class_organization"))
        elif "外协" in application_class:
            self.click_element(loc("application_class_outsourcing"))

    # 项目名称_个人
    def input_project_name(self, application_class, project_name):
        if "个人" in application_class:
            self.input_text(loc("project_name_personage"), project_name)
        elif "组织" in application_class:
            self.input_text(loc("project_name_organization"), project_name)

    # 开始时间
    def click_start_time(self):
        self.click_element(loc("start_time"))

    # 结束时间
    def click_end_time(self):
        self.click_element(loc("end_time"))

    # 选中时间
    def click_select_time(self):
        self.click_element(loc("select_time"))

    # 存储容量
    def input_storage_capacity(self, storage_capacity):
        self.input_text(loc("storage_capacity"), storage_capacity)

    # 软件类型_全部
    def click_software_type(self):
        self.click_element(loc("software_type"))
        self.click_element(loc("software_all"))

    # 添加软件
    def click_add_software(self):
        self.click_element(loc("add_software"))

    # 选中软件
    def click_select_software(self, software_name):
        self.click_element(loc("software_list"))
        if "cgg" in software_name:
            self.click_element(loc("select_cgg"))
        elif "omega" in software_name:
            self.click_element(loc("select_omega"))
        elif "mtsoft2d" in software_name:
            self.click_element(loc("select_mtsoft2d"))
        elif "test1" in software_name:
            self.click_element(loc("select_test1"))
        elif "test2" in software_name:
            self.click_element(loc("select_test2"))

    # 备注
    def input_note(self, note):
        self.input_text(loc("note"), note)

    # 提交
    def click_submit(self):
        self.click_element(loc("submit"))

    # 二次确认
    def click_reconfirm(self, select_software):
        if "mtsoft2d" in select_software:
            self.click_element(loc("reconfirm"))

    # 编辑选中
    def click_select_edit_audit(self):
        self.click_element(loc("select_edit_audit"))

    # 编辑按钮
    def click_button_edit(self):
        self.click_element(loc("button_edit"))

    # 催办
    def click_button_hasten(self):
        self.click_element(loc("button_hasten"))

    # 删除
    def click_button_delete(self):
        self.click_element(loc("button_delete"))

    # 撤回
    def click_button_recall(self):
        self.click_element(loc("button_recall"))

    # 待审核
    def click_wait_audit(self):
        self.click_element(loc("wait_audit"))

    # 审核通过
    def click_audit_pass(self, num=None):
        if num is not 2:
            self.click_element(loc("audit_pass"))
        else:
            self.click_element(loc("audit_refuse"))

    # 资源授权
    def click_audit_manage(self):
        self.click_element(loc("resource_auth"))

    # 浏览
    def click_browse(self):
        self.click_element(loc("browse"))

    # 选中资源组
    def click_select_resource_group(self):
        self.click_element(loc("select_resource_group"))

    # 完成
    def click_finish(self):
        self.click_element(loc("finish"))

    # 再次确认
    def click_confirm_again(self):
        self.click_element(loc("confirm_again"))

    # 已通过模块
    def click_pass_module(self):
        self.click_element(loc("module_pass"))

    # 提交模块
    def click_submit_module(self):
        self.click_element(loc("module_submit"))

    # 审批记录
    def click_examine_record(self):
        self.click_element(loc("module_examine"))