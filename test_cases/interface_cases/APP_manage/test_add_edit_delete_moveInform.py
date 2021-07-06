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
        
        @allure.step("接口test_addOrUpdHomePageManage")
        def test_addOrUpdHomePageManage(self):
            payload1 = {
                        'accessToken':config.TOKEN,
                        'content': {
                                    'description': "APP位置-我的-消息中心页",
                                    'informContent': "1111111111111111",
                                    'informUri': "llczd://www.services.czd.com.cn/m/mine/message",
                                    'offlineTime': None,
                                    'onlineTime': "2021-06-01 00:00:00"
                                    }
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url+'/cms-api/infoManage/addOrUpdHomePageManage', data=payload1,headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200,'test_addOrUpdHomePageManage')

        @allure.step("接口test_selInformManageList")
        def test_selInformManageList(self):
            payload1 = {
                'accessToken': config.TOKEN,
                'content': {},
                "page": {"pageNum": 1, "pageSize": 20}
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/inform/selInformManageList', data=payload1,
                               headers=headers)

            global value
            value=r1.json()['content']['list'][0]['informId']
            return(value)

        @allure.step("接口test_addOrUpdHomePageManage")
        def test_addOrUpdHomePageManage(self):
            payload1 = {
                'accessToken': config.TOKEN,
                'content': {
                    'description': "APP位置-我的-消息中心页",
                    'informContent': "1111111122222222",
                    'informId': value,
                    'informUri': "llczd://www.services.czd.com.cn/m/mine/message",
                    'offlineTime': None,
                    'onlineTime': "2021-06-01 00:00:00",
                    'sortNum': "-32"
                }
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/infoManage/addOrUpdHomePageManage', data=payload1,
                               headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200, 'test_addOrUpdHomePageManage')

        @allure.step("接口test_updInformManageState")
        def test_updInformManageState(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "content": {
                    'informId': value,
                    'state': "0"
                }
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/inform/updInformManageState', data=payload1,
                               headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200, 'updInformManageState')

        @allure.step("接口test_updInformManageMobile")
        def test_updInformManageMobile(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "content": {
                    'informId': value,
                    'type': 2
                }
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/inform/updInformManageMobile', data=payload1,
                               headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200, 'updInformManageMobile')

        @allure.step("接口test_delInformManage")
        def test_delInformManage(self):
                payload1 = {
                            'accessToken': config.TOKEN,
                            "content": [value]
                }
                headers = {
                            "Content-Type": "application/json"
                            }
                payload1 = json.dumps(payload1)
                r1 = requests.post(url=config.Pre_Url + '/cms-api/inform/delInformManage', data=payload1,
                               headers=headers)
                As = AssertUtil()
                As.assert_code(r1.json()['code'], 200, 'delInformManage')

if __name__ == "__main__":
    pytest.main(['-s', 'test_add_edit_delete_moveInform'])
