# -*- coding: utf-8 -*-
import requests
import pytest
import allure
from base import config
import json
from base.AssertUtil import AssertUtil
from test_cases.interface_cases import conftest
import time
import random
import random
import random
#@pytest.mark.usefixture("test_getToken")
class TestCase():
        value=1

        @allure.step("接口test_addPopInfo")
        def test_addPopInfo(self):
            payload1 = {
                'accessToken':config.TOKEN,
                "content": {
                                'appType': "1",
                                'endShowTime': 253402185600000,
                                'materialCode': "PIC234242653615869952",
                                'materialSonId': 1383,
                                'popLocationList': [{
                                'oneLevel': "A", 'twoLevel': "A", 'checked': 'false'},
                                 {'oneLevel': "C", 'twoLevel': "A", 'checked': 'true'},
                                {'oneLevel': "D", 'twoLevel': "A", 'checked': 'false'},
                                {'oneLevel': "B", 'twoLevel': "A", 'checked': 'false'},
                                {'oneLevel': "F", 'twoLevel': "A", 'checked': 'false'}],
                                'popName': "test弹窗",
                                'popType': 1,
                                'pushUserCity': [],
                                'pushUserRegisterTime': None,
                                'pushUserSex': [],
                                'pushUserStockAge': [],
                                'pushUserUlabelId': [],
                                'startShowTime': 1623686400000,
                                'targetUserType': "3"
                            }
            }

            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url+'/cms-api/pop/addPopInfo', data=payload1,headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200,'addPopInfo')

        @allure.step("接口test_selPopList")
        def test_selPopList(self):
            payload1 = {
                "accessToken": config.TOKEN,
                "page": {"pageNum": 1, "pageSize": 20},
                "content": {"appType": "",
                            "creator": None,
                            "endCreateTime": None,
                            "popName": None,
                            "popStatus": 0,
                            "popType": 0,
                            "startCreateTime": None}
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/pop/selPopList', data=payload1, headers=headers)
            global value
            value = r1.json()['content']['list'][0]['popId']
            return (value)

        @allure.step("接口test_updatePopInfo")
        def test_updatePopInfo(self):
            payload1 = {
                'accessToken':config.TOKEN,
                "content": {
                                'appType': "1",
                                'endShowTime': 253402185600000,
                                'materialCode': "PIC234242653615869952",
                                'materialSonId': 1383,
                                'popId':value,
                                'popLocationList': [{
                                'oneLevel': "A", 'twoLevel': "A", 'checked': 'false'},
                                 {'oneLevel': "C", 'twoLevel': "A", 'checked': 'true'},
                                {'oneLevel': "D", 'twoLevel': "A", 'checked': 'false'},
                                {'oneLevel': "B", 'twoLevel': "A", 'checked': 'false'},
                                {'oneLevel': "F", 'twoLevel': "A", 'checked': 'false'}],
                                'popName': "test弹窗"+str(random.randint(1,9999)),
                                'popType': 1,
                                'pushUserCity': [],
                                'pushUserRegisterTime': None,
                                'pushUserSex': [],
                                'pushUserStockAge': [],
                                'pushUserUlabelId': [],
                                'startShowTime': 1623686400000,
                                'targetUserType': "3"
                            }
            }
            print(payload1)
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url+'/cms-api/pop/updatePopInfo', data=payload1,headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200,'test_updatePopInfo')

        @allure.step("接口test_usePopById")
        def test_usePopById(self):
            payload1 = {
                'accessToken':config.TOKEN,
                "content": {'popId':value}
            }

            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url+'/cms-api/pop/usePopById', data=payload1,headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200,'usePopById')


if __name__ == "__main__":
    pytest.main(['-s', 'test_add_edit_closePop'])
