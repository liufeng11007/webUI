# -*- coding: UTF-8 -*-
# @time     : 2020-11-27 9:37
# @Auther   : Aaron
# @File     : kaifa_page.py

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class KaiFa(BasePage):
    url = "http://staging.ukuaiqi.com/dashboard#customers/my/list"

    # 点击 新建开发客户
    create = (By.XPATH, '//*[@class="m0 create"]')

    # 输入客户名称
    name = (By.XPATH, '//input[@placeholder="请输入客户名称"]')
    # 输入客户详细地址
    address = (By.XPATH, '//input[@placeholder="请输入客户详细地址"]')
    # 输入网址
    website = (By.XPATH, '//input[@placeholder="请输入网址"]')
    # 输入客户来源
    customer_form = (By.XPATH, '//input[@placeholder="请输入客户来源，限50字以内"]')
    # 输入星级-整数
    input_int = (By.XPATH, '//input[@placeholder="请输入整数"]')
    # 输入伺服与运动控制-小数
    input_float = (By.XPATH, '//input[@placeholder="请输入小数"]')
    # 输入主要联系邮箱
    input_email = (By.XPATH, '//input[@placeholder="请输入邮箱"]')
    # 输入客户简介
    introduction = (By.XPATH, '//*[@placeholder="请简要输入客户描述或者公司客户"]')
    # 输入客户创建日期
    input_date = (By.XPATH, '//*[@placeholder="请选择日期"]')
    # 输入理发店撒时间
    input_time = (By.XPATH, '//*[@placeholder="请选择时间" and @id="t4"]')
    # 输入龙卷风日期时间
    data_tiem = (By.XPATH, '//*[@placeholder="请选择时间" and @id="n4"]')
    # 输入客户电话
    phone = (By.XPATH, '//*[@placeholder="请输入电话" and @id="t7"]')
    """新建联系人开关"""
    # 点击新建联系人开关
    on_off = (By.XPATH, '//*[@class="loyo-switcher"]')
    # 新建联系人
    # 输入姓名
    name_contact = (By.XPATH, '//*[text()="联系人信息 "]/../../../div[2]/div[1]/div[2]/input')
    # 输入手机
    phone_contact = (By.XPATH, '//*[text()="联系人信息 "]/../../../div[2]/div[2]/div/div[2]/div[2]/input')
    # 输入座机
    call_contact = (By.XPATH, '//*[text()="联系人信息 "]/../../../div[2]/div[3]/div/div/div[2]/div[2]/input')
    # 输入部门职务
    dept_contact = (By.XPATH, '//*[text()="联系人信息 "]/../../../div[2]/div[4]/div[2]/input')
    # 输入QQ
    qq_contact = (By.XPATH, '//*[text()="联系人信息 "]/../../../div[2]/div[5]/div[2]/input')
    # 输入微信
    wchat_contact = (By.XPATH, '//*[text()="联系人信息 "]/../../../div[2]/div[7]/div[2]/input')
    # 输入E-Mail
    email_contact = (By.XPATH, '//*[text()="联系人信息 "]/../../../div[2]/div[8]/div[2]/input')

    # 点击提交
    commit = (By.XPATH, '//*[text()="提 交"]')

    # 添加联系人
    add_contact = (By.XPATH, '//*[text()="添加联系人"]')

    # 获取必填或格式错误提示信息
    tip = (By.XPATH, '//*[@class="mr-sm"]/../span[2]')
    # 获取创建成功提示信息
    success_tip = (By.XPATH, '//*[@class="modal-body-container text-center  "]/div')


    def get(self):
        self.driver.get(self.url)
        return self

    def click_create(self):
        self.find(self.create).click()
        return self

    def create_customer(self, test_info):
        self.find_and_send(self.name, test_info["name"])
        self.find_and_send(self.address, test_info["address"])
        self.find_and_send(self.website, test_info["website"])
        self.find_and_send(self.customer_form, test_info["customer_form"])
        self.find_and_send(self.input_int, test_info["input_int"])
        self.find_and_send(self.input_float, test_info["input_float"])
        self.find_and_send(self.input_email, test_info["input_email"])
        self.find_and_send(self.introduction, test_info["introduction"])
        self.find_and_send(self.input_date, test_info["input_date"])
        self.find_and_send(self.input_time, test_info["input_time"])
        self.find_and_send(self.data_tiem, test_info["data_tiem"])
        self.find_and_send(self.phone, test_info["phone"])

    def click_create_contact(self):
        self.find(self.on_off).click()

    def create_contact(self, test_info):
        self.find_and_send(self.name_contact, test_info["name_contact"])
        self.find_and_send(self.phone_contact, test_info["phone_contact"])
        self.find_and_send(self.call_contact, test_info["call_contact"])
        self.find_and_send(self.dept_contact, test_info["dept_contact"])
        self.find_and_send(self.qq_contact, test_info["qq_contact"])
        self.find_and_send(self.wchat_contact, test_info["wchat_contact"])
        self.find_and_send(self.email_contact, test_info["email_contact"])

    def click_commit(self):
        self.find(self.commit).click()
        return self

    def click_add_contact(self):
        self.find(self.add_contact).click()
        return self

    def get_tip(self):
        tip = self.find(self.tip)
        return tip.text

    def get_success_tip(self):
        tip = self.find(self.success_tip)
        return tip.text

    def get(self):
        self.driver.get(self.url)







