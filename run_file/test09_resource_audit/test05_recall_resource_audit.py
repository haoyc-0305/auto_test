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

    # 撤回资源申请
    def test_recall_resource_application(self):
        audit_number = self.audit.get_text(resource_audit.loc("resource_audit_number"))
        self.audit.click_button_recall()
        self.audit.not_text_element(resource_audit.loc("resource_audit_number"), audit_number, "【撤回资源申请】")


if __name__ == '__main__':
    pytest.main(["-s", "test05_recall_resource_audit.py"])