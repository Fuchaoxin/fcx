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

        @allure.step("接口test_addNavigationbarInfo")
        def test_addNavigationbarInfo(self):
            payload1 = {
                'accessToken':config.TOKEN,
                "content": {
                                'appType': "1",
                                'endShowTime': 1717171200000,
                                'materialCode': "PIC217700278085132288",
                                'materialSonId': 1291,
                                'navigationbarName': "test导航条",
                                'oneLevel': "A",
                                'onePcLevel': "",
                                'pushUserCity': [],
                                'pushUserRegisterTime': None,
                                'pushUserSex': [],
                                'pushUserStockAge': [],
                                'pushUserUlabelId': [],
                                'startShowTime': 1622476800000,
                                'targetUserType': "1",
                                'twoLevel': "A"
                            }
            }

            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url+'/cms-api/navigationbar/addNavigationbarInfo', data=payload1,headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200,'addNavigationbarInfo')

        @allure.step("接口test_selNavigationbarList")
        def test_selNavigationbarList(self):
            payload1 = {
                "accessToken": config.TOKEN,
                "page": {"pageNum": 1, "pageSize": 20},
                "content": {"appType": "",
                            "creator": None,
                            "endCreateTime": None,
                            "navigationbarName": None,
                            "navigationbarStatus": 0,
                            "oneLevel": "",
                            "startCreateTime": None,
                            "twoLevelName": ""}
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/navigationbar/selNavigationbarList', data=payload1,
                               headers=headers)
            global value
            value = r1.json()['content']['list'][0]['navigationbarId']
            return (value)

        @allure.step("接口test_updateNavigationbarInfo")
        def test_updateNavigationbarInfo(self):
            payload1 = {
                'accessToken':config.TOKEN,
                "content": {
                                'appType': "1",
                                'endShowTime': 1717171200000,
                                'materialCode': "PIC217700278085132288",
                                'materialSonId': 1291,
                                'navigationbarName': "test导航条",
                                'oneLevel': "A",
                                'navigationbarId': value,
                                'pushUserCity': [],
                                'pushUserRegisterTime': None,
                                'pushUserSex': [],
                                'pushUserStockAge': [],
                                'pushUserUlabelId': [],
                                'startShowTime': 1622476800000,
                                'targetUserType': "1",
                                'twoLevel': "A"
                            }
            }
            print(payload1)
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url+'/cms-api/navigationbar/updateNavigationbarInfo', data=payload1,headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200,'updateNavigationbarInfo')

        @allure.step("接口test_useNavigationbarById")
        def test_useNavigationbarById(self):
            payload1 = {
                'accessToken':config.TOKEN,
                "content": {'navigationbarId':value}
            }

            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url+'/cms-api/navigationbar/useNavigationbarById', data=payload1,headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200,'useNavigationbarById')


if __name__ == "__main__":
    pytest.main(['-s', 'test_add_edit_closeNavigationbar'])
