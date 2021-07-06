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
#@pytest.mark.usefixture("test_getToken")
class TestCase():
        value=1

        @allure.step("接口test_special_add")
        def test_special_add(self):
            payload1 = {
                        'accessToken':config.TOKEN,
                        "content": {'brief': "11111111111111111111",
                                    'imageUrl': "https://oss.caizidao.com.cn/rpdt/specialColumn_manage/750%26280.png",
                                    'name': "testf",
                                    'payTips': "111111111111111111111111111111"
                            }
            }

            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url+'/ssax-cls-cms-api/special/add', data=payload1,headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200,'test_special_add')


        @allure.step("接口test_specialList")
        def test_specialList(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "page": {"pageNum": 0, "pageSize": 10},
                "content": {}
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/ssax-cls-cms-api/special/list', data=payload1, headers=headers)
            global value
            value= r1.json()['content']['list'][0]['id']
            print(value)
            return(value)

        @allure.step("接口test_special_startOrStopSpecial")
        def test_special_startOrStopSpecial(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "content": {
                            'isEnable': 1,
                            'id': value
                            }
            }

            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/ssax-cls-cms-api/special/startOrStopSpecial', data=payload1, headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200, 'test_special_startOrStopSpecial')

        @allure.step("接口test_specialDetail")
        def test_specialDetail(self):
            payload1 = {
                'accessToken':config.TOKEN,
                "content": {
                                'id': value
                }
            }

            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url+'/ssax-cls-cms-api/special/detail', data=payload1,headers=headers)

            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200, 'specialDetail')

        @allure.step("接口test_specialedit")
        def test_specialedit(self):
            payload1 = {
                'accessToken':config.TOKEN,
                "content": {
                            'id': value,
                            'brief': "222222222222222",
                            'imageUrl': "https://oss.caizidao.com.cn/rpdt/specialColumn_manage/750%26280.png",
                            'name': "testf",
                            'payTips': "111111111111111111111111111111"
                }
            }

            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url+'/ssax-cls-cms-api/special/edit', data=payload1,headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200,'specialedit')

        @allure.step("接口test_moveSpecial")
        @pytest.mark.parametrize("type,expect_result",[(2,200),(1,200)])
        def test_moveSpecial(self,type,expect_result):
            payload1 = {
                'accessToken': config.TOKEN,
                "content": {
                    'currentMoveId': value,
                    'type': type
                }
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/ssax-cls-cms-api/special/moveSpecial', data=payload1,
                               headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], expect_result, 'moveSpecial')

        @allure.step("接口test_specialDelete")
        def test_specialDelete(self):
                payload1 = {
                            'accessToken': config.TOKEN,
                            "content": {
                            'id': value
                         }
                }
                headers = {
                            "Content-Type": "application/json"
                            }
                payload1 = json.dumps(payload1)
                r1 = requests.post(url=config.Pre_Url + '/ssax-cls-cms-api/special/delete', data=payload1,
                               headers=headers)
                As = AssertUtil()
                As.assert_code(r1.json()['code'], 200, 'specialDelete')

if __name__ == "__main__":
    pytest.main(['-s', 'test_add_close_deleteSpecial'])
