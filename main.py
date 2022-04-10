# -*- coding:utf-8 -*-
import requests
import json

# 以下为POST请求
url = 'http://120.238.246.103:60009/reverews.asmx/pay/heart?'      #接口地址
#url = 'http://192.168.5.6:60009/reverews.asmx/pay/heart?'

headers = {"Content-Type": "application/x-www-form-urlencoded"}    #如果不指定，也是默认用这个类型的

postdatas ='jsondata={"machine_id":"18AA520A","machine_ip":"192.168.0.200","machine_mac":"40204AFF18AA","sign":"76A061BCA3E649C1F94A84F14FD82AFC"}'

postdatas ='jsondata={"machine_id":"18AA520A","machine_ip":"192.168.0.200","machine_mac":"40204AFF18AA","sign":"76A061BCA3E649C1F94A84F14FD82AFC"}'


r = requests.post(url, data=postdatas,headers=headers)
print (r.status_code)           #返回状态码是200表示收到响应。
print(r.content)
'''
b'{"clear_now":0,"deal_money":0,"heart_rate":0,"ihdr":0,"interval_second":0,"living_check":0,"living_value":0,"lovertimems":0,"machine_addr":0,"open_time":0,"remote_ctrl":0,"result_code":"FAIL","return_code":"SUCCESS","return_msg":"\xe8\xae\xbe\xe5\xa4\x87\xe6\x97\xa0\xe6\x95\x88","set_iving_mode":0,"set_offline":0,"setrange":0,"update_card_count":0,"update_face_count":0,"verification":0,"work_mode":0,"write_card":0,"out_sign":null}'
'''

data1=json.loads(r.content)     #将JSON数据解码为dict（字典）
print(data1)
print(data1['clear_now'])       #打印字典中某字段数据
print(data1['return_code'])     #打印字典中某字段数据

'''
{'clear_now': 0, 'deal_money': 0, 'heart_rate': 0, 'ihdr': 0, 'interval_second': 0, 'living_check': 0, 'living_value': 0, 'lovertimems': 0, 'machine_addr': 0, 'open_time': 0, 'remote_ctrl': 0, 'result_code': 'FAIL', 'return_code': 'SUCCESS', 'return_msg': '设备无效', 'set_iving_mode': 0, 'set_offline': 0, 'setrange': 0, 'update_card_count': 0, 'update_face_count': 0, 'verification': 0, 'work_mode': 0, 'write_card': 0, 'out_sign': None}
'''

#
# data={"name":"sunxiaomin","sex":"男","年龄":"26"}
# #将python字典类型变成json数据格式
# json_str=json.dumps(data)
# print(json_str)
# print(type(json_str))
# #将JSON数据解码为dict（字典）
# data1=json.loads(json_str)
# print(data1)
# print(type(data1))
# print(data1['sex'])
