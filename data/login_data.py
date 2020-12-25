# -*- coding: UTF-8 -*-
# @time     : 2020-11-24 9:20
# @Auther   : Aaron
# @File     : login_data.py


case_success = [
    {"mobile": "17702811011", "pwd": "222111", "expected": "aaron3333"}
]

cases_error = [
    {"mobile": "", "pwd": "", "expected": "请输入用户名和密码"},
    {"mobile": "13502811019", "pwd": "123456", "expected": "手机号码或密码错误！请联系管理人员。"},
    {"mobile": "13502811011", "pwd": "123123", "expected": "手机号码或密码错误！请联系管理人员。"},
]