import os, sys
sys.path.append(os.getcwd())
import pytest
from base_file.base_driver import setup, login
from conf_file import authority_manage
from base_file.base_yaml import data_yaml


def data(key):
    return data_yaml("data_authority")[key]


class TestAuthority:

    # 打开职权管理
    def setup_class(self):
        self.driver = setup()
        self.auth = authority_manage.AuthorityManage(self.driver)
        login(self.driver)
        self.auth.open_authority()

    def teardown_class(self):
        self.driver.quit()

    # 删除职权
    def test_create_authority(self, authority_name=data("test_auto_name")):
        self.auth.click_text_authority_name()
        self.auth.click_authority_del()
        self.auth.click_authority_del_confirm()
        self.auth.displayed_false(authority_manage.loc("authority_name"), "删除职权【%s】" % authority_name)


if __name__ == '__main__':
    pytest.main(["-s", "test031_authority_delete.py"])
