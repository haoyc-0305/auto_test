import os,sys
sys.path.append(os.getcwd())
import pytest
from base_file.base_driver import setup, login
from conf_file import user_manage
from base_file.base_yaml import data_yaml


def data(key):
    return data_yaml("data_user_manage")[key]


class TestCreateRank:

    def setup(self):
        self.driver = setup()
        self.user_manage = user_manage.UserManage(self.driver)
        login(self.driver)
        self.user_manage.open_user_manage()
        
    def teardown(self):
        self.driver.quit()
    
    # 创建职级
    def test_create_rank(self, rank_name=data("test_create_rank")):
        self.user_manage.click_edit_rank()
        self.user_manage.click_rank_lower()
        self.user_manage.input_rank_name(rank_name)
        self.user_manage.click_edit_rank_confirm()
        self.user_manage.displayed_true(user_manage.loc("edit_rank_name"), "创建职级【%s】" % rank_name)


if __name__ == '__main__':
    pytest.main(["-s", "test00_rank_create.py"])


