# -*- coding: UTF-8 -*-
# @time     : 2020-12-30 14:28
# @Auther   : Aaron
# @File     : dingdan_page.py

import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from data.dingdan_data import case_khmc
from selenium import webdriver
from pages.login_page import LoginPage


class Dingdan(BasePage):
    url = "http://staging.ukuaiqi.com/dashboard#order"
    # 新建订单按钮
    xjdd = (By.XPATH, '//button[@class="btn btn-sm btn-success buried-order add-order"]')
    # 新建订单字段
    # 客户名称
    name = (By.XPATH, '//input[@placeholder="请选择客户"]')
    # click_name = (By.XPATH, '//*[text()="客户名称  "]')
    click_name = (By.XPATH, '//*[@class="cusName pull-left"][1]')

    # 购买产品-快速添加产品
    tjcp = (By.XPATH, '//*[text()="购买产品  "]/../div/a')
    # 快速添加产品-选择产品，第一个
    xzcp = (By.XPATH, '//div[@class="product-latest-list"]/div[1]/div/div[2]/div')
    # 快速添加产品-点击保存
    bc = (By.XPATH, '//*[text()="已添加产品:"]/../div[7]/button[2]')

    # 成交金额
    cjje = (By.XPATH, '//input[@placeholder="请输入成交金额"]')
    # 请输入订单标题
    ddbt = (By.XPATH, '//input[@placeholder="请输入订单标题"]')
    # 请输入订单编号
    ddbh = (By.XPATH, '//input[@placeholder="请输入订单编号"]')

    # 点击添加回款计划
    hkjh = (By.XPATH, '//*[text()="回款计划  "]/../div/a')
    # 请输入计划回款金额
    jhhkje = (By.XPATH, '//input[@placeholder="请输入计划回款金额"]')
    # 点击确定
    qd = (By.XPATH, '//form[@class="form-horizontal sale-product-madel"]/div[2]/button[2]')

    # 点击回款
    hk = (By.XPATH, '//*[text()="回款  "]/../div/a')
    # 请输入回款金额
    hkje = (By.XPATH, '//input[@placeholder="请输入回款金额"]')
    # 请输入开票金额
    kpje = (By.XPATH, '//input[@placeholder="请输入开票金额"]')
    # 点击确定
    djqd = (By.XPATH, '//form[@class="form-horizontal sale-product-madel"]/div[2]/button[2]')

    # 开始时间
    kssj = (By.XPATH, '//*[text()="开始时间  "]/../div/input')
    # 结束时间
    jssj = (By.XPATH, '//*[text()="结束时间  "]/../div/input')

    # 附件
    fj = (By.XPATH, '//input[@name="attachments"]')
    # 备注
    bz = (By.XPATH, '//textarea[@id="remark"]')
    # 点击提交订单
    tjdd = (By.XPATH, '//div[@class="modal-buttons-container"]/button[2]')

    # 创建成功提示
    tip = (By.XPATH, '//div[@class="modal-body-container text-center  "]/div')
    # 关闭提示
    close_tip = (By.XPATH, '//*[@class="modal-buttons-container"]/button[1]')

    # 必填提示
    must_tip = (By.XPATH, '//*[@class="mr-sm"]/../span[2]')

    # 全选
    qx = (By.XPATH, '//*[text()="客户名称"]/../th[1]/input')
    # 删除
    delete_b = (By.XPATH, '//*[text()="删除"]')
    # 转移订单
    zydd_b = (By.XPATH, '//*[@class="loyo-box-sekec"]/div[1]/div')
    # 添加参与人
    tjcyr_b = (By.XPATH, '//*[@class="loyo-box-sekec"]/div[2]/div')
    # 大批量操作
    dpl = (By.XPATH, '//*[@class="loyo-box-sekec"]/div[3]/button')
    # 删除全部订单
    del_all = (By.XPATH, '//*[@class="ant-dropdown-menu-item"]')
    # 确认删除
    del_qr = (By.XPATH, '//*[@class="ant-modal-footer"]/button[2]')

    # 获取订单总数量
    get_number = (By.XPATH, '//*[@class="totalRecords-span"]')

    # 提示订单创建成功，点击关闭
    # close_tip = (By.XPATH, '//*[@class="modal-buttons-container"]/button[1]')

    # 获取成交金额、回款金额、未回款金额、回款率
    get_cjje = (By.XPATH, '//*[@class="table_payment  pt pull-right"]/span[1]/span')
    get_hkje = (By.XPATH, '//*[@class="table_payment  pt pull-right"]/span[2]/span')
    get_whkje = (By.XPATH, '//*[@class="table_payment  pt pull-right"]/span[3]/span')
    get_hkl = (By.XPATH, '//*[@class="table_payment  pt pull-right"]/span[4]/span')

    def __init__(self, driver):
        self.driver = driver

    def get(self):
        time.sleep(3)
        self.driver.get(self.url)
        time.sleep(3)

    # 点击新建订单
    def click_xjdd(self, test_info):
        self.find(self.xjdd).click()
        time.sleep(1)
        # self.find_and_send(self.name, test_info["name"])
        self.find(self.name).click()
        time.sleep(2)
        self.find(self.click_name).click()
        # 添加购买产品
        self.find(self.tjcp).click()
        time.sleep(3)
        self.find(self.xzcp).click()
        self.find(self.bc).click()
        time.sleep(1)
        # 成交金额、订单标题、订单编号
        self.find(self.cjje).clear()
        self.find_and_send(self.cjje, test_info["cjje"])
        self.find_and_send(self.ddbt, test_info["ddbt"])
        self.find_and_send(self.ddbh, test_info["ddbh"])
        # 点击回款计划
        self.find(self.hkjh).click()
        time.sleep(1)
        self.find_and_send(self.jhhkje, test_info["jhhkje"])
        self.find(self.qd).click()
        # 点击回款
        self.find(self.hk).click()
        time.sleep(1)
        self.find_and_send(self.hkje, test_info["hkje"])
        self.find_and_send(self.kpje, test_info["kpje"])
        self.find(self.djqd).click()
        # 开始时间
        self.find_and_send(self.kssj, test_info["kssj"])
        # 结束时间
        self.find_and_send(self.jssj, test_info["jssj"])
        # 附件
        time.sleep(1)
        self.find(self.fj).send_keys(r"D:\Pictures\11111.png")
        time.sleep(5)
        # 备注
        self.find_and_send(self.bz, test_info["bz"])
        # 点击提交订单
        self.find(self.tjdd).click()
        time.sleep(2)

    # 获取成功提示信息
    def get_tip(self):
        time.sleep(3)
        tip = self.find(self.tip).text
        time.sleep(1)
        self.find(self.close_tip).click()
        return tip

    # 获取必填提示信息
    def get_error_tips(self):
        time.sleep(1)
        tip = self.find(self.must_tip).text
        return tip

    def create_khmc(self, test_info):
        self.find(self.xjdd).click()
        time.sleep(2)
        # 添加购买产品
        self.find(self.tjcp).click()
        time.sleep(2)
        self.find(self.xzcp).click()
        self.find(self.bc).click()
        time.sleep(1)
        # 成交金额、订单标题、订单编号
        self.find(self.cjje).clear()
        self.find_and_send(self.cjje, test_info["cjje"])
        self.find_and_send(self.ddbt, test_info["ddbt"])
        self.find_and_send(self.ddbh, test_info["ddbh"])
        # 点击回款计划
        self.find(self.hkjh).click()
        time.sleep(1)
        self.find_and_send(self.jhhkje, test_info["jhhkje"])
        self.find(self.qd).click()
        # 点击回款
        self.find(self.hk).click()
        time.sleep(1)
        self.find_and_send(self.hkje, test_info["hkje"])
        self.find_and_send(self.kpje, test_info["kpje"])
        self.find(self.djqd).click()
        # 开始时间
        self.find_and_send(self.kssj, test_info["kssj"])
        # 结束时间
        self.find_and_send(self.jssj, test_info["jssj"])
        # 附件
        time.sleep(1)
        self.find(self.fj).send_keys(r"D:\Pictures\11111.png")
        time.sleep(5)
        # 备注
        self.find_and_send(self.bz, test_info["bz"])
        # 点击提交订单
        self.find(self.tjdd).click()
        time.sleep(2)

    def create_gmcp(self, test_info):
        # 点击新建订单按钮
        self.find(self.xjdd).click()
        time.sleep(1)
        # 选择客户
        self.find(self.name).click()
        time.sleep(2)
        self.find(self.click_name).click()
        time.sleep(1)
        # 成交金额、订单标题、订单编号
        self.find_and_send(self.cjje, test_info["cjje"])
        self.find_and_send(self.ddbt, test_info["ddbt"])
        self.find_and_send(self.ddbh, test_info["ddbh"])
        # 点击回款计划
        self.find(self.hkjh).click()
        time.sleep(1)
        self.find_and_send(self.jhhkje, test_info["jhhkje"])
        self.find(self.qd).click()
        # 点击回款
        self.find(self.hk).click()
        time.sleep(1)
        self.find_and_send(self.hkje, test_info["hkje"])
        self.find_and_send(self.kpje, test_info["kpje"])
        self.find(self.djqd).click()
        # 开始时间
        self.find_and_send(self.kssj, test_info["kssj"])
        # 结束时间
        self.find_and_send(self.jssj, test_info["jssj"])
        # 附件
        time.sleep(1)
        self.find(self.fj).send_keys(r"D:\Pictures\11111.png")
        time.sleep(5)
        # 备注
        self.find_and_send(self.bz, test_info["bz"])
        # 点击提交订单
        self.find(self.tjdd).click()
        time.sleep(2)

    def create_hkjh(self, test_info):
        self.find(self.xjdd).click()
        time.sleep(1)
        # self.find_and_send(self.name, test_info["name"])
        self.find(self.name).click()
        time.sleep(2)
        self.find(self.click_name).click()
        # 添加购买产品
        self.find(self.tjcp).click()
        time.sleep(2)
        self.find(self.xzcp).click()
        self.find(self.bc).click()
        time.sleep(1)
        # 成交金额、订单标题、订单编号
        self.find_and_send(self.cjje, test_info["cjje"])
        self.find_and_send(self.ddbt, test_info["ddbt"])
        self.find_and_send(self.ddbh, test_info["ddbh"])
        # 点击回款
        self.find(self.hk).click()
        time.sleep(1)
        self.find_and_send(self.hkje, test_info["hkje"])
        self.find_and_send(self.kpje, test_info["kpje"])
        self.find(self.djqd).click()
        # 开始时间
        self.find_and_send(self.kssj, test_info["kssj"])
        # 结束时间
        self.find_and_send(self.jssj, test_info["jssj"])
        # 附件
        time.sleep(1)
        self.find(self.fj).send_keys(r"D:\Pictures\11111.png")
        time.sleep(5)
        # 备注
        self.find_and_send(self.bz, test_info["bz"])
        # 点击提交订单
        self.find(self.tjdd).click()
        time.sleep(2)

    def create_hk(self, test_info):
        self.find(self.xjdd).click()
        time.sleep(1)
        # self.find_and_send(self.name, test_info["name"])
        self.find(self.name).click()
        time.sleep(2)
        self.find(self.click_name).click()
        # 添加购买产品
        self.find(self.tjcp).click()
        time.sleep(2)
        self.find(self.xzcp).click()
        self.find(self.bc).click()
        time.sleep(1)
        # 成交金额、订单标题、订单编号
        self.find_and_send(self.cjje, test_info["cjje"])
        self.find_and_send(self.ddbt, test_info["ddbt"])
        self.find_and_send(self.ddbh, test_info["ddbh"])
        # 点击回款计划
        self.find(self.hkjh).click()
        time.sleep(1)
        self.find_and_send(self.jhhkje, test_info["jhhkje"])
        self.find(self.qd).click()
        # 开始时间
        self.find_and_send(self.kssj, test_info["kssj"])
        # 结束时间
        self.find_and_send(self.jssj, test_info["jssj"])
        # 附件
        time.sleep(1)
        self.find(self.fj).send_keys(r"D:\Pictures\11111.png")
        time.sleep(5)
        # 备注
        self.find_and_send(self.bz, test_info["bz"])
        # 点击提交订单
        self.find(self.tjdd).click()
        time.sleep(2)

    # 全选
    def click_qx(self):
        self.find(self.qx).click()

    # 转移订单
    def zydd(self):
        self.find(self.zydd_b).click()

    # 添加参与人
    def tjcyr(self):
        self.find(self.tjcyr_b).click()

    # 删除
    def delete(self):
        self.find(self.delete_b).click()

    # 大批量操作
    def dpl_op(self):
        self.find(self.dpl).click()
        time.sleep(1)
        self.find(self.del_all).click()

    def dpl_qrsc(self):
        time.sleep(1)
        self.find(self.del_qr).click()

    # 获取订单总数量
    def get_dd_number(self):
        time.sleep(2)
        self.get()
        numb = self.find(self.get_number).text
        return numb

    # 提示订单创建成功，点击关闭
    # def close_tipw(self):
    #     time.sleep(2)
    #     self.find(self.close_tip).click()

    # 获取成交金额、回款金额、未回款金额、回款率
    def get_je_info(self):
        self.get()
        time.sleep(2)
        cjje = self.find(self.get_cjje).text
        hkje = self.find(self.get_hkje).text
        whkje = self.find(self.get_whkje).text
        hkl = self.find(self.get_hkl).text
        return cjje, hkje, whkje, hkl


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.maximize_window()
    test_login = LoginPage(driver)
    # test_login.login("17702811011", "22211")
    test_login.login("17702811011", "222111")
    time.sleep(3)
    dd = Dingdan(driver)
    dd.get()
    dd.create_khmc(case_khmc[0])
    print(case_khmc[0]["expected"])
    tip = dd.get_error_tips()
    print(tip)
    if tip == case_khmc[0]["expected"]:
        print("yes")
    else:
        print("no")




