# -*- coding: UTF-8 -*-
# @time     : 2020-11-24 17:27
# @Auther   : Aaron
# @File     : 1124.py


def test(dict1):
    print(dict1)
    print(dict1["name"])

    # print(data["name"])
data = [
    {"name": "qqewe", "cname": "1234"}
]
# print(data[0])

test(data[0])

# import pytest
# from pages.home_page import HomePage
# from pages.crm.xiansuo import XianSuo
# from data.xiansuo_data import case_success
#
#
# @pytest.mark.xiansuo
# class Test_Xiansuo:
#     @pytest.mark.parametrize("test_info", case_success)
#     def test_xinjian(self, test_info):
#         print(test_info)
#         print(test_info["name"])
#         assert test_info==test_info["name"]

