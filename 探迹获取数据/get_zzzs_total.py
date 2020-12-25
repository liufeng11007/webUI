# -*- coding: UTF-8 -*-
# @time     : 2020-12-08 19:44
# @Auther   : Aaron
# @File     : get_zzzs_total.py

import requests, json
from rw_excel import RW_Excel
from requests_toolbelt import MultipartEncoder


class Request:

    def __init__(self):
        self.session = requests.Session()

    def send(self, method, url, **kwargs):
        return self.session.request(method, url, **kwargs)

    def add_header(self, one_dict):
        self.session.headers.update(one_dict)

    def close(self):
        self.session.close()


if __name__ == '__main__':
    filename = r"F:\工作\竞品测试\get_zzzs.xlsx"
    sheetname = "jzy"
    do_excel = RW_Excel(filename, sheetname)
    testcases = do_excel.read_data()
    print(testcases)
    one_testcase = testcases[0]

    form_data = {
        "filter": '{"must":[{"hasMobile":[{"exist":"'+str(one_testcase.hasMobile)+'"}]},{"address":[{"eq":[["'+one_testcase.address+'"]]}]},{"hasCertificate":[{"exist":"'+str(one_testcase.hasCertificate)+'"}]},{"certNameList":[{"eq":[["'+one_testcase.groups+'","'+one_testcase.zs_name+'"]]}]}]}'
    }

    data1 = {
        "filter":'{"must":[{"hasMobile":[{"exist":"1"}]},{"address":[{"eq":[["云南"]]}]},{"hasCertificate":[{"exist":"1"}]},{"certNameList":[{"eq":[["建筑业企业资质","古建筑工程专业承包二级"],["建筑业企业资质","市政公用工程施工总承包三级"]]}]}]}'
             }
    m = {
        "filter": '{"must":[{"hasCertificate":[{"exist":"1"}]}]}'
    }

    # print(m["filter"]["must"][0]["hasCertificate"][0]["exist"])
    # print(json.dumps(m))

    header_dict = {
        # "accept": "*/*",
        # "accept-encoding": "gzip, deflate, br",
        # "accept-language": "zh-CN,zh;q=0.9",
        # "cache-control": "no-cache",
        # "content-type": "multipart/form-data; boundary=----WebKitFormBoundaryl57bHPezTiAo79aQ",
        # "content-type":  "application/json; charset=utf-8",
        "cookie": "_bl_uid=qRkgFg7h3C220vjjau8Uu9jlbsnk; _ga=GA1.2.822939062.1605149792; Hm_lvt_d3ee3af8af62f47558a292277356e90f=1605660866,1605753825,1606889867,1607395507; Hm_lpvt_d3ee3af8af62f47558a292277356e90f=1607395507; _gid=GA1.2.1316320368.1607395508; Hm_lvt_f2ee75449fc055cc4dbceb4fe403bea3=1606889883,1606979025,1607395517,1607414723; Hm_lpvt_f2ee75449fc055cc4dbceb4fe403bea3=1607417054; accountCenterSessionId=.eJwtkE1PwzAMhv9LzjvkO_bOSGgSLQIqpHKpEsfR1lZFWgeMIf47GXB-_fix3y-xMOdhje88nF6HnMS2xHnljXhb-TgcstgKxwoUIIG2ichxMey9kUlsxPo70HTz2Or-_DI2p_amd_dPUvZdf77rJtlcdqemm3R7efjsx-dDc_s4VZD2cVl4rvAHXxf9mdAZCeRSctmW5BljrM5A6DFQVIVROc4OQSeyBQEiBQCGaEM2MhStyKBxRVLONoG1oMHnYLx2Hk2FuCQ0ueYJVVAOKVlMAWxR9bUcroeUI6_7_xa-fwDgLlZD.ErHJgQ.UW24fczhP1plE05Q5vtJiaIyUUE",
        # "origin": "https://sales.tungee.com",
        # "pragma": "no-cache",
        "referer": "https://sales.tungee.com/customer-seeking/advanced-filter/enterprise",
        # "user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3823.400 QQBrowser/10.7.4307.400"
    }
    # r = Request()
    # r.add_header(header_dict)
    # aa = r.send("POST", one_testcase.url, data=form_data)
    r = requests.post(one_testcase.url, headers=header_dict, data=form_data)
    print(r.json())
    print(r.json()["total"])














