import os, sys
sys.path.append(os.getcwd())
import pytest
from base_file.base_driver import setup,login
from base_file.base_yaml import data_yaml
from conf_file import resource_audit


def data(key):
    return data_yaml("data_resource_audit")[key]


class TestAdminAuditManage:

    # 打开管理员审批管理
    def setup_class(self, module_info=data("audit_config")):
        self.driver = setup()
        self.audit = resource_audit.ResourceAudit(self.driver)
        login(self.driver)
        self.audit.open_resource_application(module_info["module_type"])

    def teardown_class(self):
        self.driver.quit()

    # 资源授权
    def test_resource_auth(self):
        wait_audit_number = self.audit.get_element_num(resource_audit.loc("resource_auth"))
        num = 0
        while num < wait_audit_number:
            audit_number = self.audit.get_text(resource_audit.loc("resource_au dit_number"))
            self.audit.click_audit_manage()
            self.audit.click_browse()
            self.audit.click_select_resource_group()
            self.audit.click_finish()
            self.audit.click_confirm_again()
            self.audit.not_text_element(resource_audit.loc("resource_audit_number"), audit_number, "【管理员资源授权】")
            num += 1


if __name__ == '__main__':
    pytest.main(["-s", "test04_admin_audit_manage.py"])