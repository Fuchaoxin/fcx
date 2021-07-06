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

value = 1
value1 = 1
class TestCase():

        @allure.step("接口test_insertLabelCategory")
        def test_insertLabelCategory(self):
            payload1 = {
                        'accessToken':config.TOKEN,
                        "content": {
                            'labelId': None,
                            'labelLevel': 1,
                            'labelName': "qq",
                            'userName': ""
                            }
            }

            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url+'/cms-api/labelCategoryManage/insertLabelCategory', data=payload1,headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200,'test_insertLabelCategory')

        @allure.step("接口test_getLabelCategoryList")
        def test_getLabelCategoryList(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "content": {'labelId': None,
                            'labelLevel': 1,
                            'labelName': "qq",
                            'userName': ""
                            }
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/labelCategoryManage/getLabelCategoryList', data=payload1, headers=headers)
            a=len(r1.json()['content'])
            global value
            value=r1.json()['content'][a-1]['labelId']
            return(value)

        @allure.step("接口test_insertLabelCategory1")
        def test_insertLabelCategory1(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "content": {
                    'labelId': value,
                    'labelLevel': 1,
                    'labelName': "q1",
                    'userName': ""
                }
            }

            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/labelCategoryManage/insertLabelCategory', data=payload1,
                               headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200, 'test_insertLabelCategory1')

        @allure.step("接口test_getLabelCategoryList1")
        def test_getLabelCategoryList1(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "content": {'labelId': value,
                            'labelLevel': 1,
                            'labelName': "q1",
                            'userName': ""
                            }
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/labelCategoryManage/getLabelCategoryList', data=payload1,
                               headers=headers)
            a = len(r1.json()['content'])
            global value1
            value1 = r1.json()['content'][a - 1]['labelId']
            print("value1=",value1)
            return (value1)

        @allure.step("接口test_updateLabelCategoryName")
        def test_updateLabelCategoryName(self):
            payload1 = {
                'accessToken':config.TOKEN,
                "content": {
                    'labelId': value,
                    'labelLevel': 1,
                    'labelName': "ss",
                    'userName': "bailingyu"

                }
            }

            headers = {
                "Content-Type": "application/json"
            }

            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url+'/cms-api/labelCategoryManage/updateLabelCategoryName', data=payload1,headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200,'updateLabelCategoryName')


        @allure.step("接口test_deleteLabelCategoryList")
        def test_deleteLabelCategoryList(self):
                payload1 = {
                            'accessToken': config.TOKEN,
                            "content": {
                                        'children':{'labelId': value1,
                                                    'labelLevel': 2,
                                                    'labelName': "q1",
                                                    'userName': ""
                                                    },
                                        'labelId': value,
                                        'labelLevel': 1,
                                        'labelName': "ss",
                                        'userName': ""
                         }
                }
                headers = {
                            "Content-Type": "application/json"
                            }
                print (value)
                payload1 = json.dumps(payload1)
                r1 = requests.post(url=config.Pre_Url + '/cms-api/labelCategoryManage/deleteLabelCategoryList', data=payload1,
                               headers=headers)
                As = AssertUtil()
                As.assert_code(r1.json()['code'], 200, 'deleteLabelCategoryList')

if __name__ == "__main__":
    pytest.main(['-s', 'test_add_delete_labelCategory'])
