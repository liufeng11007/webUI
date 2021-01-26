# -*- coding: UTF-8 -*-
# @time     : 2020-12-07 15:40
# @Auther   : Aaron
# @File     : gonghai_page.py

import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys


class Gonghai(BasePage):

    url = "http://staging.ukuaiqi.com/dashboard#customer-public"

    # 公海客户总数
    total_numb = (By.XPATH, '//span[@class="totalRecords-span"]')

    # 全选
    qx_button = (By.XPATH, '//div[@class="header_container"]/table/thead/tr/th/input')
    # 勾选全选选中的数量
    qx_sl = (By.XPATH, '//em[@class="select-number"]')
    # 批量挑入
    p_tr = (By.XPATH, '//button[text()="批量挑入"]')
    qd_button = (By.XPATH, '//button[text()="确认"]')
    # 挑入成功提示
    tr_tip = (By.XPATH, '//div[@role="alert"]/span[2]')

    # 删除
    p_sc = (By.XPATH, '//button[text()="删除"]')
    scqr_bu = (By.XPATH, '//div[@class="modal-buttons-container"]/button[3]')
    # 删除提示
    sc_tip = (By.XPATH, '//div[@role="alert"]/span[2]')

    # 获取客户名称
    name_kh = (By.XPATH, '//*[@class="customer-row"][1]/td[2]')

    # 通过客户名称搜索公海客户
    search_kh = (By.XPATH, '//input[@id="term-ipt"]')
    # 按回车
    # driver.find_element_by_xpath('//input[@id="term-ipt"]').send_keys(Keys.ENTER)

    # 大批量操作
    dplcz = (By.XPATH, '//button[@class="ant-btn ant-dropdown-trigger"]')
    qbsc = (By.XPATH, '//li[@class="ant-dropdown-menu-item"]')
    # 大批量删除确认
    dplscqr = (By.XPATH, '//div[@class="ant-modal-footer"]/button[3]')

    def __init__(self, driver):
        self.driver = driver

    def get(self):
        time.sleep(3)
        self.driver.get(self.url)
        time.sleep(3)

    # 获取公海客户总量、搜索后的数量
    def ghkh_total(self):
        # time.sleep(3)
        total = self.find(self.total_numb).text
        return total

    # 勾选全选选项按钮
    def click_qx(self):
        time.sleep(3)
        self.find(self.qx_button).click()

    # 返回已选中的数量
    def qx_number(self):
        time.sleep(1)
        qx_number = self.find(self.qx_sl).text
        return qx_number

    # 批量挑入
    def pltr(self):
        time.sleep(1)
        self.find(self.p_tr).click()
        time.sleep(1)
        # 确认操作
        self.find(self.qd_button).click()

    # 批量删除
    def delet_pl(self):
        self.find(self.p_sc).click()
        time.sleep(1)
        # 确认操作
        self.find(self.scqr_bu).click()

    # 批量挑入、删除提示
    def get_tips(self):
        time.sleep(2)
        tip = self.find(self.tr_tip).text
        return tip

    # 获取客户名称
    def get_name(self):
        name = self.find(self.name_kh).text
        return name

    # 通过客户名称搜索公海客户
    def search_ghkh(self, search_words):
        # self.get()
        self.find(self.search_kh).clear()
        self.find_and_send(self.search_kh, search_words)
        self.find_and_send(self.search_kh, Keys.ENTER)

    # 大批量操作
    def dpl_operation(self):
        self.find(self.dplcz).click()
        time.sleep(1)
        self.find(self.qbsc).click()
        time.sleep(1)
        # 确认操作
        self.find(self.dplscqr).click()

