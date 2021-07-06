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
       
        @allure.step("接口test_addLabelCate")
        def test_addLabelCate(self):
            payload1 = {
                'accessToken':config.TOKEN,
                "content": {
                                'name': "123"
                            }
            }

            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url+'/cms-api/labelManage/addLabelCate', data=payload1,headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 1,'addLabelCate')

        @allure.step("接口test_getLabelCateList")
        def test_getLabelCateList(self):
            payload1 = {
                'accessToken': config.TOKEN
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/labelManage/getLabelCateList', data=payload1,
                               headers=headers)
            global value
            value = r1.json()['content'][0]['id']
            return (value)

        @allure.step("接口test_editLabelCate")
        def test_editLabelCate(self):
            payload1 = {
                'accessToken':config.TOKEN,
                "content": {
                                'id': value,
                                'name': "1231"
                            }
            }
            print(payload1)
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url+'/cms-api/labelManage/editLabelCate', data=payload1,headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 1,'editLabelCate')

        @allure.step("接口test_editLabelCate")
        def test_editLabelCate(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "content": {
                    'id': value,
                    'isDeleted': 1
                }
            }
            print(payload1)
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/labelManage/editLabelCate', data=payload1,
                               headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 1, 'editLabelCate')


if __name__ == "__main__":
    pytest.main(['-s', 'test_add_edit_deleteLabelCate'])
