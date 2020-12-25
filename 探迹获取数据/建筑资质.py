# -*- coding: UTF-8 -*-
# @time     : 2020-12-03 15:18
# @Auther   : Aaron
# @File     : 建筑资质.py


import requests

url = "https://sales.tungee.com/api/follow-up-leads?task_type=lead_follow_up_robot_call&sort_field=follow_up_status_update_time&sort=-1&follow_up_status_update_time_begin=1606924800000&follow_up_status_update_time_end=1607011199999&begin=200&end=400&page_offset=1&prev_search_after=%5B1606979359209%2C%2257c7bb19ed332d74%22%5D&next_search_after=%5B1606979347947%2C%2237623023f1ff32cf%22%5D"

header = {
    "cookie": "_bl_uid=qRkgFg7h3C220vjjau8Uu9jlbsnk; _ga=GA1.2.822939062.1605149792; Hm_lvt_d3ee3af8af62f47558a292277356e90f=1605253066,1605660866,1605753825,1606889867; _gid=GA1.2.764406904.1606979021; Hm_lpvt_d3ee3af8af62f47558a292277356e90f=1606979022; Hm_lvt_f2ee75449fc055cc4dbceb4fe403bea3=1605660873,1605753833,1606889883,1606979025; Hm_lpvt_f2ee75449fc055cc4dbceb4fe403bea3=1606979086; accountCenterSessionId=.eJwljstOwzAQRf_F6y7i-DWTLa2iSiQIqYDoJvKMxy2lBClJqQDx71iwPvdxvtX8klSj9u3jW99uXL--X7q6u_Y3VbVfP3zd7l7Nvt0u3VP32Z8O7m53sM-njVErNeRJ5qNqlukiK8XHOI5yLlNXoUJHkTTM8UOG5X1IpJocz3PJDX936EwF7Ihcspm8YIy1pcDoMXDUWVA7SQ6hJrYZASIHAIFoQzJVyLVmg8blilOyBNZCDT4F42vn0ZSSZEKTCifUQTtkskgBbNaWOIUieJll-pdxokEDMhQFZifZiPemIvXzCyeMVOc.EqoiHQ.3fWAwtdcL3BUQH_TFg816-Sv1cg",
    "content-type": "application/json",
    "referer: https": "//sales.tungee.com/lead-management/lead-follow-up/by-company-name",
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3823.400 QQBrowser/10.7.4307.400"

}

res = requests.session()

res.headers.update(header)

r = res.get(url, header=header)
print(r.json())
