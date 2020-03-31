import os,sys
sys.path.append(os.getcwd())
import pytest
from base_file.base_driver import setup, login
from conf_file import user_manage
from base_file.base_yaml import data_yaml


def data(key):
    return data_yaml("data_user_manage")[key]


class TestDeleteRank:

    def setup(self):
        self.driver = setup()
        self.user_manage = user_manage.UserManage(self.driver)
        login(self.driver)
        self.user_manage.open_user_manage()
        
    def teardown(self):
        self.driver.quit()
    
    # 删除职级
    def test_delete_rank(self, rank_name=data("test_create_rank")):
        self.user_manage.click_edit_rank()
        self.user_manage.click_lower_rank()
        self.user_manage.click_delete_rank()
        self.user_manage.click_edit_rank(clrar=1)
        self.user_manage.element_number(user_manage.loc("edit_rank_name_list"), 5, "删除职级【%s】" % rank_name)


if __name__ == '__main__':
    pytest.main(["-s", "test020_rank_delete.py"])


