# -*- coding: UTF-8 -*-
# @time     : 2020-11-20 13:43
# @Auther   : Aaron
# @File     : login_page.py

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
    # click = HomePage(driver)
    # click_crm = click.click_crm_menu()
    # click_xiansou = click.click_xiaosouxiansuo()
    # driver.find_element_by_xpath('//*[@class="m0 create"]').click()
    # time.sleep(3)
    # create = XianSuo(driver)
    # create.click_xinjianxiansuo()
    # time.sleep(3)
    # create.create_xiansuo(case_success[0])
    # driver.find_element_by_xpath('//lable[text()="姓名  "]/../div/input').send_keys("fdafasg")

    url = "http://staging.ukuaiqi.com/dashboard#customer-public"
    # 公海客户总数
    total_numb = (By.XPATH, '//span[@class="totalRecords-span"]')
    # 全选
    qx_button = (By.XPATH, '//div[@class="header_container"]/table/thead/tr/th/input')
    driver.get(url)
    time.sleep(3)
    total = driver.find_element_by_xpath('//span[@class="totalRecords-span"]').text
    print("公海客户数量为：" + str(total))
    time.sleep(2)
    # 全选后批量挑入
    # driver.find_element_by_xpath('//div[@class="header_container"]/table/thead/tr/th/input').click()
    # driver.find_element_by_xpath('//button[text()="批量挑入"]').click()
    # time.sleep(1)
    # driver.find_element_by_xpath('//button[text()="确认"]').click()
    # time.sleep(2)
    # text1 = driver.find_element_by_xpath('//div[@role="alert"]/span[2]').text
    # print(text1)
    # time.sleep(2)
    # # 删除
    # driver.find_element_by_xpath('//div[@class="header_container"]/table/thead/tr/th/input').click()
    # driver.find_element_by_xpath('//button[text()="删除"]').click()
    # time.sleep(1)
    # driver.find_element_by_xpath('//div[@class="modal-buttons-container"]/button[3]').click()
    # time.sleep(1)
    # text2 = driver.find_element_by_xpath('//div[@role="alert"]/span[2]').text
    # print(text2)
    time.sleep(2)
    # 大批量操作-删除全部客户
    # driver.find_element_by_xpath('//div[@class="header_container"]/table/thead/tr/th/input').click()
    driver.find_element_by_xpath('//input[@id="term-ipt"]').send_keys("高合金钢的0034")
    driver.find_element_by_xpath('//input[@id="term-ipt"]').send_keys(Keys.ENTER)
    time.sleep(3)
    s_total = driver.find_element_by_xpath('//span[@class="totalRecords-span"]').text
    print("搜索结果数量为："+str(s_total))
    time.sleep(2)
    # driver.find_element_by_xpath('//span[text()="大批量操作 "]').click()
    driver.find_element_by_xpath('//button[@class="ant-btn ant-dropdown-trigger"]').click()
    time.sleep(2)
    # driver.find_element_by_xpath('//li[text()="删除全部客户"]').click()
    driver.find_element_by_xpath('//li[@class="ant-dropdown-menu-item"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//div[@class="ant-modal-footer"]/button[3]').click()

    time.sleep(10)
    driver.find_element_by_xpath('//input[@id="term-ipt"]').send_keys("高合金钢的0034")
    driver.find_element_by_xpath('//input[@id="term-ipt"]').send_keys(Keys.ENTER)
    time.sleep(3)
    d_total = driver.find_element_by_xpath('//span[@class="totalRecords-span"]').text
    print("大批量删除后数量为：" + str(d_total))

    time.sleep(1)
    driver.find_element_by_xpath('//input[@id="term-ipt"]').clear()
    driver.find_element_by_xpath('//input[@id="term-ipt"]').send_keys(Keys.ENTER)
    time.sleep(3)
    n_total = driver.find_element_by_xpath('//span[@class="totalRecords-span"]').text
    print("最新公海客户数量为：" + str(n_total))















