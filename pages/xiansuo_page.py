# -*- coding: UTF-8 -*-
# @time     : 2020-11-24 9:45
# @Auther   : Aaron
# @File     : xiansuo.py

from selenium.webdriver.common.by import By
from pages.home_page import HomePage
from pages.base_page import BasePage


class XianSuo(BasePage):
    url = "http://staging.ukuaiqi.com/dashboard#clues"
    # 点击新建线索
    create_elem = (By.XPATH, '//*[@class="m0 create"]/a')
    """新建线索字段"""
    # 输入姓名
    name = (By.XPATH, '//lable[text()="姓名  "]/../div/input')
    # 输入公司名称
    company_name = (By.XPATH, '//lable[text()="公司名称  "]/../div/input')
    # 输入经营范围
    jyfw = (By.XPATH, '//lable[text()="经营范围  "]/../div/textarea')
    # 输入手机
    phone = (By.XPATH, '//lable[text()="手机  "]/../div/input')
    # 输入座机
    call = (By.XPATH, '//lable[text()="座机  "]/../div/input')
    # 选择地区，先点击输入框，再选择省市区
    area = (By.XPATH, '//lable[text()="地区  "]/../div/div')
    # 输入详细地址
    address = (By.XPATH, '//lable[text()="详细地址  "]/../div/input')
    # 输入备注
    bz = (By.XPATH, '//lable[text()="备注  "]/../div/div/textarea')
    # 选择线索状态，先点击选择框，再选状态
    state = (By.XPATH, '//lable[text()="线索状态  "]/../div/div')
    """线索状态类型"""
    # 未处理
    wcl = (By.XPATH, '//lable[text()="线索状态  "]/../div/div/div/div[2]/div/div')
    # 已联系
    ylx = (By.XPATH, '//lable[text()="线索状态  "]/../div/div/div/div[2]/div/div[2]')
    # 关闭
    gb = (By.XPATH, '//lable[text()="线索状态  "]/../div/div/div/div[2]/div/div[3]')
    # 选择标签，先点击设置标签，再选择
    bq = (By.XPATH, '//lable[text()="标签  "]/../div/a')
    # 输入自定义单行文本
    zdhwb = (By.XPATH, '//lable[text()="自定义单行文本  "]/../div/input')
    # 输入自定义多行文本
    zmhwb = (By.XPATH, '//lable[text()="自定义多行文本  "]/../div/textarea')
    # 输入自定义数字
    zsz = (By.XPATH, '//lable[text()="自定义数字  "]/../div/input')
    # 输入自定义整数
    zzs = (By.XPATH, '//lable[text()="自定义整数  "]/../div/input')
    # 输入自定义日期
    zrq = (By.XPATH, '//lable[text()="自定义日期  "]/../div/input')
    # 输入自定义时间
    ztime = (By.XPATH, '//lable[text()="自定义时间  "]/../div/input')
    # 输入自定义日期+时间
    zrqsj = (By.XPATH, '//lable[text()="自定义日期+时间  "]/../div/input')
    # 输入自定义单选，先点击选择框，在选择
    zdx = (By.XPATH, '//lable[text()="自定义单选  "]/../div/a')
    # 输入自定义多选，先点击选择框，在选择
    zmx = (By.XPATH, '//lable[text()="自定义多选  "]/../div/div/div[1]')
    # 输入自定义电话
    zdh = (By.XPATH, '//lable[text()="自定义电话  "]/../div/input')
    # 输入自定义邮箱
    zemail = (By.XPATH, '//lable[text()="自定义邮箱  "]/../div/input')
    # 输入自定义网址
    zaaddr = (By.XPATH, '//lable[text()="自定义网址  "]/../div/input')

    """提交、取消"""
    # 提交按钮
    commit = (By.XPATH, '//button[text()="提交"]')
    # 提交按钮
    cancel = (By.XPATH, '//button[text()="提交"]/../button[2]')

    # 提示信息
    tips = (By.XPATH, '//*[@class="flashes__alert alert alert-danger"]/span[2]')

    # 创建成功提示信息
    success_tip = (By.XPATH, '//*[@class="modal-body-container text-center  "]/div')

    # def __init__(self, driver):
    #     self.driver = driver
    def refresh(self):
        self.driver.refresh()

    def get(self):
        self.driver.get(self.url)

    def click_xinjianxiansuo(self):
        create_but = self.driver.find_element(*self.create_elem)
        create_but.click()
        return self

    def create_xiansuo(self, test_info):
        # 输入姓名
        input_name = self.driver.find_element(*self.name)
        input_name.send_keys(test_info["name"])
        # 输入公司名称
        input_cname = self.driver.find_element(*self.company_name)
        input_cname.send_keys(test_info["company_name"])
        # 输入经营范围
        self.find_and_send(self.jyfw, test_info["jyfw"])
        # 输入手机
        self.find_and_send(self.phone, test_info["phone"])
        # 输入座机
        self.find_and_send(self.call, test_info["call"])
        # 输入详细地址
        self.find_and_send(self.address, test_info["address"])
        # 输入备注
        self.find_and_send(self.bz, test_info["bz"])
        # 输入自定义单行文本
        self.find_and_send(self.zdhwb, test_info["zdhwb"])
        # 输入自定义多行文本
        self.find_and_send(self.zmhwb, test_info["zmhwb"])
        # 输入自定义数字
        self.find_and_send(self.zsz, test_info["zsz"])
        # 输入自定义整数
        self.find_and_send(self.zzs, test_info["zzs"])
        # 输入自定义日期
        self.find_and_send(self.zrq, test_info["zrq"])
        # 输入自定义时间
        self.find_and_send(self.ztime, test_info["ztime"])
        # 输入自定义日期+时间
        self.find_and_send(self.zrqsj, test_info["zrqsj"])
        # 输入自定义电话
        self.find_and_send(self.zdh, test_info["zdh"])
        # 输入自定义邮箱
        self.find_and_send(self.zemail, test_info["zemail"])
        # 输入自定义网址
        self.find_and_send(self.zaaddr, test_info["zaaddr"])

    def click_commite(self):
        commite_elem = self.driver.find_element(*self.commit)
        commite_elem.click()
        return self

    def get_tips(self):
        """获取提示信息"""
        tip = self.find(self.tips)
        # tip.text
        return tip.text

    def create_success(self):
        success_tip = self.find(self.success_tip)
        return success_tip.text







