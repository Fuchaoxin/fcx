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
       
        @allure.step("接口test_addLabel")
        def test_addLabel(self):
            payload1 = {
                'accessToken':config.TOKEN,
                "content": {
                                'cateCode': "label3",
                                'firstVisitJgm': 'false',
                                'isDeleted': 'false',
                                'name': "12345",
                                'recmdJgmIndex': 'false',
                                'sortNum': 1
                            }
            }

            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url+'/cms-api/labelManage/addLabel', data=payload1,headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 1,'addLabel')

        @allure.step("接口test_getLabelList")
        def test_getLabelList(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "page": {"pageNum": 5, "pageSize": 20},
                "content": {
                            'cateCode': "label3",
                            'labelName': ""
                            }
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/labelManage/getLabelList', data=payload1, headers=headers)
            a=len(r1.json()['content']['list'])
            global value
            value = r1.json()['content']['list'][a-1]['id']
            return (value)

        @allure.step("接口test_editLabel")
        def test_editLabel(self):
            payload1 = {
                'accessToken':config.TOKEN,
                "content": {
                                'id': value,
                                 'cateCode':'b0ed136d8f1c41279b6e774724c84161'
                            }
            }
            print(payload1)
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url+'/cms-api/labelManage/editLabel', data=payload1,headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200,'editLabel')

        @allure.step("接口test_editLabel")
        def test_editLabel(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "content": {
                    'id': value,
                    'isCommonTags': "1"
                }
            }
            print(payload1)
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/labelManage/editLabel', data=payload1, headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200, 'editLabel')

        @allure.step("接口test_editLabel")
        def test_editLabel(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "content": {
                    'id': value,
                    'isDeleted': 'true'
                }
            }
            print(payload1)
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/labelManage/editLabel', data=payload1, headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200, 'editLabel')

if __name__ == "__main__":
    pytest.main(['-s', 'test_add_edit_deleteLabelList'])
