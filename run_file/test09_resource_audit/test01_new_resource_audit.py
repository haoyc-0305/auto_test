import os, sys
sys.path.append(os.getcwd())
import pytest
from base_file.base_driver import setup,login
from base_file.base_yaml import data_yaml
from conf_file import resource_audit


def data(key):
    return data_yaml("data_resource_audit")[key]


class TestNewResourceAudit:

    # 打开资源申请
    def setup_class(self, login_info=data("open_resource_audit")):
        self.driver = setup()
        self.audit = resource_audit.ResourceAudit(self.driver)
        login(self.driver, user_name=login_info["user_name"], user_pass=login_info["user_pass"])
        self.audit.open_resource_application(login_info["module_type"])

    def teardown_class(self):
        self.driver.quit()

    # 新建资源申请
    @pytest.mark.parametrize("application_info", data("new_resource_application"))
    def test_new_resource_application(self, application_info):
        audit_number = self.audit.get_text(resource_audit.loc("resource_audit_number"))
        self.audit.click_new_resource_application()
        self.audit.click_application_class(application_info["application_class"])
        self.audit.input_project_name(application_info["application_class"], application_info["project_name"])
        self.audit.click_start_time()
        self.audit.click_select_time()
        self.audit.click_end_time()
        self.audit.click_select_time()
        self.audit.input_storage_capacity(application_info["storage_capacity"])
        self.audit.click_software_type()
        self.audit.click_add_software()
        self.audit.click_select_software(application_info["select_software"])
        self.audit.input_note(application_info["project_name"])
        self.audit.click_submit()
        self.audit.click_reconfirm(application_info["select_software"])
        self.audit.not_text_element(resource_audit.loc("resource_audit_number"), audit_number, "新建资源申请【%s】"
                                    % application_info["select_software"])


if __name__ == '__main__':
    pytest.main(["-s", "test01_audit_config.py"])