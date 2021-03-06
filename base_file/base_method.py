import cx_Oracle
import pymysql
import os
import time
import win32gui
from time import sleep
import win32con
from selenium.webdriver import ActionChains
from base_file.base_file_route import image_path, download_path, upload_path, database
image = image_path()
download = download_path()
upload = upload_path()
oracle = database()["oracle"]
mysql = database()["mysql"]


class Method:

    def __init__(self, driver):
        self.driver = driver

    # 点击操作
    def click_element(self, loc, clear=None):
        if clear is None:
            sleep(0.2)
        else:
            sleep(clear)
        self.find_element(loc).click()

    # 输入操作
    def input_text(self, loc, text, clear=None):
        if clear is None:
            sleep(0.2)
        else:
            sleep(1)
        self.find_element(loc).clear()
        self.find_element(loc).send_keys(text)

    # 鼠标悬停
    def mouse_element(self, loc):
        Action = ActionChains(self.driver)
        Action.move_to_element(self.find_element(loc)).perform()
        sleep(1)

    # 获取元素文本
    def get_text(self, loc):
        sleep(0.5)
        loc_text = self.find_element(loc).text
        return loc_text

    # 获取元素数量
    def get_element_num(self, loc):
        by = loc[0]
        value = loc[1]
        element_num = self.driver.find_elements(by, value)
        return len(element_num)

    # 判断元素存在
    def displayed_true(self, loc, text):
        sleep(2)
        try:
            self.find_element(loc)
            is_true = True
        except:
            is_true = False
            new_time = time.strftime("%Y-%m-%d_%H-%M-%S")
            self.driver.get_screenshot_as_file(image + "%s%s.png" % (new_time, text))
        print("%s:" % text, is_true)

    # 判断元素不存在
    def displayed_false(self, loc, text):
        sleep(2)
        try:
            self.find_element(loc)
            is_true = False
            new_time = time.strftime("%Y-%m-%d_%H-%M-%S")
            self.driver.get_screenshot_as_file(image + "%s%s.png" % (new_time, text))
        except:
            is_true = True
        print("%s:" % text, is_true)

    # 判断元素已选中
    def selected_true(self, loc, text):
        sleep(2)
        try:
            is_true = self.find_element(loc).is_selected()
            print("%s:" % text, is_true)
            assert is_true
        except:
            new_time = time.strftime("%Y-%m-%d_%H-%M-%S")
            self.driver.get_screenshot_as_file(image + "%s%s.png" % (new_time, text))

    # 判断元素未选中
    def selected_false(self, loc, text):
        sleep(2)
        try:
            is_true = self.find_element(loc).is_selected()
            print("%s:" % text, is_true is False)
            assert not is_true
        except:
            new_time = time.strftime("%Y-%m-%d_%H-%M-%S")
            self.driver.get_screenshot_as_file(image + "%s%s.png" % (new_time, text))

    # 通过元素数量相等判断
    def element_number(self, loc, number, text):
        sleep(2)
        try:
            by = loc[0]
            value = loc[1]
            number_element = self.driver.find_elements(by, value)
            print("%s:" % text, len(number_element) == int(number))
            assert len(number_element) == int(number)
        except:
            new_time = time.strftime("%Y-%m-%d_%H-%M-%S")
            self.driver.get_screenshot_as_file(image + "%s%s.png" % (new_time, text))

    # 通过元素数量不等判断
    def not_element_number(self, loc, number, text):
        sleep(2)
        try:
            by = loc[0]
            value = loc[1]
            number_element = self.driver.find_elements(by, value)
            print("%s:" % text, len(number_element) != int(number))
            assert len(number_element) != int(number)
        except:
            new_time = time.strftime("%Y-%m-%d_%H-%M-%S")
            self.driver.get_screenshot_as_file(image + "%s%s.png" % (new_time, text))

    # 通过元素文本相等判断
    def text_element(self, loc, text, text_name):
        sleep(2)
        try:
            get_text = self.find_element(loc).text
            print("%s:" % text_name, get_text == text)
            assert get_text == text
        except:
            new_time = time.strftime("%Y-%m-%d_%H-%M-%S")
            self.driver.get_screenshot_as_file(image + "%s%s.png" % (new_time, text_name))

    # 通过元素文本不相等判断
    def not_text_element(self, loc, text, text_name):
        sleep(2)
        try:
            get_text = self.find_element(loc).text
            print("%s:" % text_name, get_text != text)
            assert get_text != text
        except:
            new_time = time.strftime("%Y-%m-%d_%H-%M-%S")
            self.driver.get_screenshot_as_file(image + "%s%s.png" % (new_time, text_name))

    # 数据库操作
    def data_run(self, statements, db_type=None):
        db = cx_Oracle.connect(oracle)
        if db_type is not None:
            db = pymysql.connect(host=mysql[0], port=int(mysql[1]), user=mysql[2], passwd=mysql[3], db=mysql[4], charset='utf8')
        cr = db.cursor()
        for sql in statements:
            try:
                if isinstance(statements, str):
                    sql = statements
                cr.execute(sql)
                if "select" in sql or "SELECT" in sql:
                    value = cr.fetchall()[0]
                    print("【数据库返回：%s】" % value[0])
                    return value[0]
                else:
                    db.commit()
                if isinstance(statements, str):
                    break
            except:
                print("【%s】执行失败！" % sql)
                break
        cr.close()
        db.close()

    # 判断文件是否下载成功，delete为空删除下载文件
    def file_find(self, name, delete=None):
        sleep(5)
        a = os.walk(download)
        file_path = download + name
        for file_list in a:
            b = 0
            for file_name in file_list[2]:
                if name in file_name:
                    print("下载【%s】:" % name, name == file_name)
                    b += 1
                    break
            if b == 1:
                break
            if b == 0:
                new_time = time.strftime("%Y-%m-%d_%H-%M-%S")
                self.driver.get_screenshot_as_file(image + "%s%s.png" % (new_time, name))
                break
        if delete is None:
            if os.path.exists(file_path):
                os.remove(file_path)
            else:
                print("没有找到文件【%s】" % name)

    # 删除下载的文件
    def delete_windows_file(self, file_name):
        file_path = download + file_name
        print(file_path)
        if os.path.exists(file_path):
            os.remove(file_path)
        else:
            print("没有找到文件【%s】" % file_path)

    # 上传文件
    def file_upload(self, file_name, wait=None):
        loc_name = None
        file_path = upload + file_name
        if "chrome" in str(self.driver):
            loc_name = "打开"
        elif "firefox" in str(self.driver):
            loc_name = "文件上传"
        elif"ie" in str(self.driver):
            loc_name = "选择要加载的文件"
        sleep(2)
        # 一级顶层窗口，此处title为上传窗口名称，浏览器不一样上传窗口名称不一样
        dialog = win32gui.FindWindow("#32770", loc_name)
        # 二级窗口
        ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)
        # 三级窗口
        ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)
        # 四级窗口
        edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)
        button = win32gui.FindWindowEx(dialog, 0, 'Button', "打开(&O)")
        # 执行操作 输入文件路径
        win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, file_path)
        # 点击打开上传文件
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)
        if wait is None:
            sleep(10)
        elif wait is not None:
            sleep(wait)

    # 元素操作
    def find_element(self, loc):
        if len(loc) == 2:
            by = loc[0]
            value = loc[1]
            return self.driver.find_element(by, value)
        elif len(loc) == 3:
            by = loc[0]
            value = loc[1]
            location = int(loc[2])
            return self.driver.find_elements(by, value)[location]
