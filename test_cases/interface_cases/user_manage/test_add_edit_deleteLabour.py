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

class TestCase():
        value=1
        
        @allure.step("接口test_addlabour")
        def test_addlabour(self):
            payload1 = {
                'accessToken':config.TOKEN,
                "content": {
                                'name': "7778888"
                            }
            }

            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url+'/cms-api/labour/add', data=payload1,headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200,'addlabour')

        @allure.step("接口test_labour_findLabourList")
        def test_labour_findLabourList(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "page": {"pageNum": 0, "pageSize": 20},
                "content": {'creater': ""
                            }
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/labour/findLabourList', data=payload1, headers=headers)
            global value
            value = r1.json()['content']['list'][0]['id']
            return (value)

        @allure.step("接口test_labour_edit")
        def test_labour_edit(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "page": {"pageNum": 0, "pageSize": 20},
                "content": {
                                'id': value,
                                'name': "77788881111"
                            }
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/labour/edit', data=payload1, headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200, 'test_labour_edit')

        @allure.step("接口test_updateUserLabourUnion")
        def test_updateUserLabourUnion(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "content": {
                    'labourUnionId': value,
                    'userIdList': ["cf27d9e2-69a1-42a2-b550-248299724dd3"]
                }
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/kol/updateUserLabourUnion', data=payload1, headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200, 'test_updateUserLabourUnion')

        @allure.step("接口test_delete")
        def test_delete(self):
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
            r1 = requests.post(url=config.Pre_Url + '/cms-api/labour/delete', data=payload1,
                               headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200, 'delete')


if __name__ == "__main__":
    pytest.main(['-s', 'test_add_edit_deleteLabour'])
