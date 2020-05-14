import os, sys
sys.path.append(os.getcwd())
import pytest
from base_file.base_driver import setup,login
from base_file.base_yaml import data_yaml
from conf_file import resource_audit


def data(key):
    return data_yaml("data_resource_audit")[key]


class TestAuditConfig:

    # 打开资源申请
    def setup_class(self, module_info=data("audit_config")):
        self.driver = setup()
        self.audit = resource_audit.ResourceAudit(self.driver)
        login(self.driver)
        self.audit.open_resource_application(module_info["module_type"])

    def teardown_class(self):
        self.driver.quit()

    # 审批配置
    def test_audit_config(self):
        self.audit.click_audit_config()
        self.audit.click_department_list()
        self.audit.click_select_department()
        self.audit.click_add_department()
        self.audit.click_level_one_audit()
        self.audit.click_juji()
        self.audit.click_level_one_chuji()
        self.audit.click_level_one_approver()
        self.audit.click_level_two_audit()
        self.audit.click_juji()
        self.audit.click_level_two_chuji()
        self.audit.click_level_two_approver()
        self.audit.click_save()
        self.driver.refresh()
        self.audit.click_audit_config()
        self.audit.displayed_true(resource_audit.loc("config_check"), "【审批配置】")


if __name__ == '__main__':
    pytest.main(["-s", "test00_audit_config.py"])