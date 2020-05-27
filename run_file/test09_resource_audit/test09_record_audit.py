import os, sys
sys.path.append(os.getcwd())
import pytest
from base_file.base_driver import setup,login
from base_file.base_yaml import data_yaml
from conf_file import resource_audit


def data(key):
    return data_yaml("data_resource_audit")[key]


class TestRecallResourceAudit:

    # 打开资源申请
    def setup_class(self, login_info=data("open_resource_audit")):
        self.driver = setup()
        self.audit = resource_audit.ResourceAudit(self.driver)
        login(self.driver, user_name=login_info["user_name"], user_pass=login_info["user_pass"])
        self.audit.open_resource_application(login_info["module_type"])

    def teardown_class(self):
        self.driver.quit()

    # 已通过记录
    def test_pass_record(self):
        self.audit.click_pass_module()
        self.audit.element_number(resource_audit.loc("pass_record"), data("pass_record"), "【已通过记录】")

    # 提交记录
    def test_submit_record(self):
        self.audit.click_submit_module()
        self.audit.element_number(resource_audit.loc("submit_record"), data("submit_record"), "【提交记录】")

    # 审批记录
    def test_examine_record(self):
        self.audit.examine_manage()
        self.audit.click_examine_record()
        self.audit.element_number(resource_audit.loc("examine_record"), data("examine_record"), "【审批人记录】")


if __name__ == '__main__':
    pytest.main(["-s", "test09_record_audit.py"])