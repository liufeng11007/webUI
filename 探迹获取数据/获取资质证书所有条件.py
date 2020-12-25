# -*- coding: UTF-8 -*-
# @time     : 2020-12-08 17:11
# @Auther   : Aaron
# @File     : 获取资质证书所有条件.py

from rw_excel import RW_Excel
import requests

res = requests.Session()


res_url = "https://sales.tungee.com/api/advance-search/configs"
header_dict = {
    "cookie": "_bl_uid=qRkgFg7h3C220vjjau8Uu9jlbsnk; _ga=GA1.2.822939062.1605149792; remember_token=5be5c3fb824bcc7d6ebd69df|8cec488aeb0a5b88ca2163737bf91b8c0fbc7e57ce8d68717275c91ca82272d0649aa13e9374ca9c30c9bcc8197feaf91b0873e6ed73fa6089197fc2c4518479; Hm_lvt_d3ee3af8af62f47558a292277356e90f=1607647949,1607995531,1608166815,1608608271; Hm_lpvt_d3ee3af8af62f47558a292277356e90f=1608616190; Hm_lvt_f2ee75449fc055cc4dbceb4fe403bea3=1608608309,1608616197,1608616833,1608626305; doncusSessionId=eyJfZnJlc2giOmZhbHNlLCJ1c2VyX2lkIjoiNWE2NWIxZjBmYjYxNWMyNmRhNDNjODUzIn0.EsRu8Q.A4Lq-PZSde5HXyDzsYoz5yHSxik; Hm_lpvt_f2ee75449fc055cc4dbceb4fe403bea3=1608703375; accountCenterSessionId=.eJwlzctKxDAYBeB3yXoWae7pWhwKtsOIIs6m5L-EWtoKbUdHxHc3KJzld875Fn1eeRtEva9XPggc0rLwJGrxySAOYmGmfksf3O_vPYGoc5q24rY3KuYyP-vTXXO7HNv9dGx1-yVlOza3h5f7uRub_TKfq9enx6kdu6Ebz7oMXjde-7-yBbaoMwRlANGTYyAXKRf0D5IE5ACJTIhe6xx90M4q4wNaS1kpl0BZIpTRV8xgZawMsLQyQQgOObqsLZtIlIMKyhtEUy5NRqeRUtDWeLAlRvkAxicVMVtyKWuXkhQ_v8HfVlw.EsRvCw.HfcT9Ffut3SVdTKcGlwdeocLUZg",
    "referer": "https://sales.tungee.com/customer-seeking/advanced-filter/enterprise"
}

res.headers.update(header_dict)


resurlt = res.request("GET", res_url)
print(len(resurlt.json()["input_values"]["contactSource"]))
group_len = len(resurlt.json()["input_values"]["contactSource"])
print(resurlt.json()["input_values"]["contactSource"][0]["first_level"])
cd = (len(resurlt.json()["input_values"]["contactSource"][0]["second_level"]))


filename = r"F:\工作\竞品测试\各省手机号渠道为官网的.xlsx"
sheetname = "qd"

w = RW_Excel(filename, sheetname)

# 多级分类
for j in range(0, group_len):
    b_len = len(resurlt.json()["input_values"]["contactSource"][j]["second_level"])
    for i in range(0, b_len):
        if i == 0:
            get_data = resurlt.json()["input_values"]["contactSource"][j]["first_level"]
            w.write_data(1, get_data)
            get_data1 = (resurlt.json()["input_values"]["contactSource"][j]["second_level"][i])
            w.write_data(2, get_data1)
        else:
            get_data = (resurlt.json()["input_values"]["contactSource"][j]["second_level"][i])
            w.write_data(2, get_data)
        # print(get_data)


# 只有一级
# sb_len = len(resurlt.json()["input_values"]["tmInternationalClassList"])
# for i in range(0, sb_len):
#     get_data = resurlt.json()["input_values"]["tmInternationalClassList"][i]
#     w.write_data(2, get_data)

