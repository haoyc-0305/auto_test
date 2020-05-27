import os, sys
sys.path.append(os.getcwd())
import pytest
from base_file.base_driver import setup,login
from base_file.base_yaml import data_yaml
from conf_file import resource_audit


def data(key):
    return data_yaml("data_resource_audit")[key]


class TestEditResourceAudit:

    # 打开资源申请
    def setup_class(self, login_info=data("open_resource_audit")):
        self.driver = setup()
        self.audit = resource_audit.ResourceAudit(self.driver)
        login(self.driver, user_name=login_info["user_name"], user_pass=login_info["user_pass"])
        self.audit.open_resource_application(login_info["module_type"])

    def teardown_class(self):
        self.driver.quit()

    # 编辑资源申请
    def test_edit_resource_application(self):
        self.audit.click_select_edit_audit()
        self.audit.click_button_edit()
        self.audit.input_storage_capacity(data("storage_capacity"))
        self.audit.click_submit()
        self.audit.displayed_true(resource_audit.loc("loc_verify"), "【编辑资源申请】")


if __name__ == '__main__':
    pytest.main(["-s", "test02_edit_resource_audit.py"])