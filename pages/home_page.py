# -*- coding: UTF-8 -*-
# @time     : 2020-11-23 17:39
# @Auther   : Aaron
# @File     : home_page.py

from selenium.webdriver.common.by import By


class HomePage:
    # 首页定位元素
    # 用户名定位
    user_name = (By.XPATH, '//div[@class="user-name"]')

    # crm_elem = (By.XPATH, '//*[@id="accordion"]/div[2]/a/div')
    crm_elem = (By.XPATH, '//*[@class="loyo-icon navbar-icon icon-CRM"]/..')
    xiansuo_eleme = (By.ID, "002001")

    def __init__(self, driver):
        self.driver = driver

    def get_user_account(self):
        user_name = self.driver.find_element(*self.user_name)
        return user_name.text

    def click_crm_menu(self):
        crm_menu = self.driver.find_element(*self.crm_elem)
        crm_menu.click()
        return self

    def click_xiaosouxiansuo(self):
        xiansuo = self.driver.find_element(*self.xiansuo_eleme)
        xiansuo.click()
        return self

