from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains

url = "http://10.1.1.37:8080"


def setup():
    driver = webdriver.Chrome()
    # 浏览器最大化
    driver.maximize_window()
    # 隐式等待30秒
    driver.implicitly_wait(10)
    # 打开浏览器
    driver.get(url)
    return driver


def login(webdriver, user_name="admin", user_pass="111111"):
    driver = webdriver
    driver.find_element_by_css_selector("[type='text']").send_keys(user_name)
    driver.find_element_by_css_selector("[type='password']").send_keys(user_pass)
    driver.find_element_by_css_selector(".el-button--primary").click()


def teardown(webdriver):
    driver = webdriver
    Action = ActionChains(driver)
    Action.move_to_element(driver.find_element_by_css_selector(".el-dropdown-selfdefine")).perform()
    sleep(1)
    driver.find_element_by_css_selector(".el-dropdown-menu__item--divided").click()
    sleep(0.5)
    driver.quit()
