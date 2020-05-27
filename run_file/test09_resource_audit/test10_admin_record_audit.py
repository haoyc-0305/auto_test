import os, sys
sys.path.append(os.getcwd())
import pytest
from base_file.base_driver import setup,login
from base_file.base_yaml import data_yaml
from conf_file import resource_audit


def data(key):
    return data_yaml("data_resource_audit")[key]


class TestAdminRecordAudit:

    # 打开管理员审批管理
    def setup_class(self, module_info=data("audit_config")):
        self.driver = setup()
        self.audit = resource_audit.ResourceAudit(self.driver)
        login(self.driver)
        self.audit.open_resource_application(module_info["module_type"])

    def teardown_class(self):
        self.driver.quit()

    # 审批记录
    def test_record_audit(self):
        self.audit.examine_manage()
        self.audit.click_examine_record()
        self.audit.element_number(resource_audit.loc("examine_record"), data("examine_record"), "【管理员记录】")


if __name__ == '__main__':
    pytest.main(["-s", "test10_admin_record_audit.py"])