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

class TestCase():
        value=1

        @allure.step("接口test_addOpenScreenPageInfo")
        def test_addOpenScreenPageInfo(self):
            payload1 = {
                'accessToken':config.TOKEN,
                "content": {
                             'adOpenScreenPageName': "test广告页"+str(random.randint(1,9999)),
                             'endShowTime': 253402185600000,
                             'materialCode': "PIC225551883643957248",
                             'materialSonId': 1314,
                             'pushUserCity': [],
                             'pushUserRegisterTime': None,
                             'pushUserSex': [],
                             'pushUserStockAge': [],
                             'pushUserUlabelId': [],
                             'showStayTime': "2",
                             'startShowTime': 1622476800000
                            }
            }

            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url+'/cms-api/adOpenScreen/addOpenScreenPageInfo', data=payload1,headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200,'addOpenScreenPageInfo')

        @allure.step("接口test_selAdOpenScreenPageList")
        def test_selAdOpenScreenPageList(self):
            payload1 = {
                "accessToken": config.TOKEN,
                "page": {"pageNum": 1, "pageSize": 20},
                "content": {"adOpenScreenPageName": None,
                            "adOpenScreenStatus": 0,
                            "creator": None,
                            "endCreateTime": None,
                            "startCreateTime": None}
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/adOpenScreen/selAdOpenScreenPageList', data=payload1,
                               headers=headers)
            global value
            value = r1.json()['content']['list'][0]['adOpenScreenPageId']
            return (value)

        @allure.step("接口test_updateSortNum")
        def test_updateSortNum(self):
            payload1 = {
                'accessToken':config.TOKEN,
                "content": {
                                'openScreenPageId': value,
                                'sortNum': random.randint(21,999)
                            }
            }
            print(payload1)
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url+'/cms-api/adOpenScreen/updateSortNum', data=payload1,headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200,'test_updateSortNum')

        @allure.step("接口test_useAdOpenScreenPageById")
        def test_useAdOpenScreenPageById(self):
            payload1 = {
                'accessToken':config.TOKEN,
                "content": {'adOpenScreenId':value}
            }

            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url+'/cms-api/adOpenScreen/useAdOpenScreenPageById', data=payload1,headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200,'useAdOpenScreenPageById')


if __name__ == "__main__":
    pytest.main(['-s', 'test_add_edit_closeOpenScreenPage'])
