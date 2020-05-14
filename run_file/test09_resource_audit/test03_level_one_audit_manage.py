import os, sys
sys.path.append(os.getcwd())
import pytest
from base_file.base_driver import setup,login
from base_file.base_yaml import data_yaml
from conf_file import resource_audit


def data(key):
    return data_yaml("data_resource_audit")[key]


class TestAuditManage:

    # 打开资源申请
    def setup_class(self, login_info=data("open_audit_manage")[1]):
        self.driver = setup()
        self.audit = resource_audit.ResourceAudit(self.driver)
        login(self.driver, user_name=login_info["user_name"], user_pass=login_info["user_pass"])
        self.audit.open_resource_application(login_info["module_type"])

    def teardown_class(self):
        self.driver.quit()

    # 一级审批管理
    def test_audit_manage(self):
        wait_audit_number = self.audit.get_element_num(resource_audit.loc("wait_audit_number"))
        num = 0
        while num < wait_audit_number:
            audit_number = self.audit.get_text(resource_audit.loc("resource_audit_number"))
            self.audit.click_wait_audit()
            self.audit.click_audit_pass()
            self.audit.not_text_element(resource_audit.loc("resource_audit_number"), audit_number, "【一级审批管理】")
            num += 1


if __name__ == '__main__':
    pytest.main(["-s", "test03_level_one_audit_manage.py"])