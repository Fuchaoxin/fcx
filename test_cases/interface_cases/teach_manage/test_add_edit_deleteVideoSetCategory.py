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
        
        @allure.step("接口test_addVideoSetCategory")
        def test_addVideoSetCategory(self):
            payload1 = {
                'accessToken':config.TOKEN,
                "page": {"pageNum": 0, "pageSize": 0},
                "content": {
                                'name': "test",
                                'parentId': 1,
                                'sortNum': 1
                            }
            }

            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url+'/cms-api/cms/videoset/category/addVideoSetCategory', data=payload1,headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200,'addVideoSetCategory')

        @allure.step("接口test_queryVideoSetCategories")
        def test_queryVideoSetCategories(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "page": {"pageNum": 0, "pageSize": 0},
                "content": {
                            'expand': 'false',
                            'parentId': 0
                            }
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/cms/videoset/category/queryVideoSetCategories', data=payload1, headers=headers)
            global value
            value = r1.json()['content'][1]['id']
            print(value)
            return (value)

        @allure.step("接口test_updateVideoSetCategory")
        def test_updateVideoSetCategory(self):
            payload1 = {
                'accessToken':config.TOKEN,
                "content": {
                                'children': [],
                                'code': "",
                                'createTime': None,
                                'creater': None,
                                'id': value,
                                'indexImage': None,
                                'isDeleted': None,
                                'modifyTime': None,
                                'name': "test",
                                'parentId': 1,
                                'sortNum': 2,
                                'type': None,
                            }
            }
            print(payload1)
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url+'/cms-api/cms/videoset/category/updateVideoSetCategory', data=payload1,headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200,'updateVideoSetCategory')


        @allure.step("接口test_deleteVideoSetCategory")
        def test_deleteVideoSetCategory(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "content": value
            }
            print(payload1)
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/cms/videoset/category/deleteVideoSetCategory', data=payload1, headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200, 'deleteVideoSetCategory')

if __name__ == "__main__":
    pytest.main(['-s', 'test_add_edit_deleteVideoSetCategory'])
