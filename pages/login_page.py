# -*- coding: UTF-8 -*-
# @time     : 2020-11-20 13:43
# @Auther   : Aaron
# @File     : login_page.py

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home_page import HomePage
from pages.xiansuo_page import XianSuo
from data.xiansuo_data import case_success


class LoginPage:
    url = "http://staging.ukuaiqi.com/login"

    username = (By.ID, "user_username")
    password = (By.ID, "user_password")
    login_btn = (By.NAME, "commit")

    error_msg = (By.XPATH, '//span[@class="text-dangers"]')

    def __init__(self, driver):
        self.driver = driver

    def get(self):
        self.driver.get(self.url)

    def login(self, mobile, pwd):
        self.get()
        time.sleep(3)
        username_elem = self.driver.find_element(*self.username)
        username_elem.send_keys(mobile)

        pws = self.driver.find_element(*self.password)
        pws.send_keys(pwd)
        # time.sleep(2)
        commit = self.driver.find_element(*self.login_btn)
        commit.click()

    def erroe_msg_elem(self):
        e = self.driver.find_element(*self.error_msg)
        return e.text


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.maximize_window()

    test_login = LoginPage(driver)
    # test_login.login("17702811011", "22211")
    test_login.login("17702811011", "222111")
    time.sleep(3)
    click = HomePage(driver)
    click_crm = click.click_crm_menu()
    click_xiansou = click.click_xiaosouxiansuo()
    # driver.find_element_by_xpath('//*[@class="m0 create"]').click()
    time.sleep(3)
    create = XianSuo(driver)
    create.click_xinjianxiansuo()
    time.sleep(3)
    create.create_xiansuo(case_success[0])
    # driver.find_element_by_xpath('//lable[text()="姓名  "]/../div/input').send_keys("fdafasg")







