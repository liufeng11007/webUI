# -*- coding: UTF-8 -*-
# @time     : 2020-12-31 10:10
# @Auther   : Aaron
# @File     : dingdan_test.py


import pytest, time

from pages.dingdan_page import Dingdan
from data.dingdan_data import case_success, case_fail, case_khmc, case_gmcp, case_hk, case_hkjh


@pytest.mark.staging
@pytest.mark.dingdan
class Test_Dingdan:
    # @pytest.mark.skip
    @pytest.mark.parametrize("test_info", case_success)
    def test_success(self, test_info, login):
        create_dd = Dingdan(login)
        create_dd.get()
        create_dd.click_xjdd(test_info)
        tip = create_dd.get_tip()
        je_info = create_dd.get_je_info()
        try:
            assert test_info["expected"] == tip
            assert test_info["cjje"] == je_info[0]
            assert test_info["hkje"] == je_info[1]

            print("测试用例通过！")
        except AssertionError as e:
            print(f"测试用例不同：{e}")
            raise e

    # @pytest.mark.skip
    @pytest.mark.parametrize("test_info", case_fail)
    def test_fail(self, test_info, login):
        create_dd = Dingdan(login)
        create_dd.get()
        create_dd.click_xjdd(test_info)
        tip = create_dd.get_error_tips()
        # print(tip)
        try:
            assert test_info["expected"] == tip
            print("测试用例通过！")
        except AssertionError as e:
            print(f"测试用例不同：{e}")
            raise e

    # 提示 请输入客户名称
    # @pytest.mark.skip
    @pytest.mark.parametrize("test_info", case_khmc)
    def test_khmc(self, test_info, login):
        create_dd = Dingdan(login)
        create_dd.get()
        create_dd.create_khmc(test_info)
        tip = create_dd.get_error_tips()
        print(tip)
        print(test_info["expected"])
        try:
            assert test_info["expected"] == tip
            print("测试用例通过！")
        except AssertionError as e:
            print(f"测试用例不同：{e}")
            raise e

    # 提示  至少添加一条产品信息
    # @pytest.mark.skip
    @pytest.mark.parametrize("test_info", case_gmcp)
    def test_gmcp(self, test_info, login):
        create_dd = Dingdan(login)
        create_dd.get()
        create_dd.create_gmcp(test_info)
        tip = create_dd.get_error_tips()
        print(tip)
        try:
            assert test_info["expected"] == tip
            print("测试用例通过！")
        except AssertionError as e:
            print(f"测试用例不同：{e}")
            raise e

    # 提示 至少添加一条回款信息
    # @pytest.mark.skip
    @pytest.mark.parametrize("test_info", case_hk)
    def test_hk(self, test_info, login):
        create_dd = Dingdan(login)
        create_dd.get()
        create_dd.create_hk(test_info)
        tip = create_dd.get_error_tips()
        print(tip)
        try:
            assert test_info["expected"] == tip
            print("测试用例通过！")
        except AssertionError as e:
            print(f"测试用例不同：{e}")
            raise e

    # 提示 至少添加一条回款计划
    # @pytest.mark.skip
    @pytest.mark.parametrize("test_info", case_hkjh)
    def test_hkjh(self, test_info, login):
        create_dd = Dingdan(login)
        create_dd.get()
        create_dd.create_hkjh(test_info)
        tip = create_dd.get_error_tips()
        print(tip)
        try:
            assert test_info["expected"] == tip
            print("测试用例通过！")
        except AssertionError as e:
            print(f"测试用例不同：{e}")
            raise e

    # @pytest.mark.skip
    def test_zydd(self, login):
        create_dd = Dingdan(login)
        create_dd.get()
        create_dd.zydd()
        tip = create_dd.get_error_tips()
        try:
            assert " 请选择订单  " == tip
            print("测试用例通过！")
        except AssertionError as e:
            print(f"测试用例不同：{e}")
            raise e

    # @pytest.mark.skip
    def test_tjcyr(self, login):
        create_dd = Dingdan(login)
        create_dd.get()
        create_dd.tjcyr()
        tip = create_dd.get_error_tips()
        try:
            assert " 请选择订单  " == tip
            print("测试用例通过！")
        except AssertionError as e:
            print(f"测试用例不同：{e}")
            raise e

    # @pytest.mark.skip
    def test_sc(self, login):
        create_dd = Dingdan(login)
        create_dd.get()
        create_dd.delete()
        tip = create_dd.get_error_tips()
        try:
            assert " 请选择订单  " == tip
            print("测试用例通过！")
        except AssertionError as e:
            print(f"测试用例不同：{e}")
            raise e

    # @pytest.mark.skip
    def test_dpl_op(self, login):
        create_dd = Dingdan(login)
        create_dd.get()
        create_dd.dpl_op()
        create_dd.dpl_qrsc()
        numb = create_dd.get_dd_number()
        try:
            assert int(numb) == 0
            print("测试用例通过！")
        except AssertionError as e:
            print(f"测试用例不同：{e}")
            raise e

    # @pytest.mark.skip
    def test_dpl_op2(self, login):
        create_dd = Dingdan(login)
        create_dd.get()
        create_dd.dpl_op()
        tip = create_dd.get_error_tips()
        try:
            assert " 大批量操作数量不能为0  " == tip
            print("测试用例通过！")
        except AssertionError as e:
            print(f"测试用例不同：{e}")
            raise e



