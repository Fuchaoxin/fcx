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
        
        @allure.step("接口test_add")
        def test_add(self):
            payload1 = {
                'accessToken':config.TOKEN,
                "content": {
                                'answer': "B",
                                'content': "test11111",
                                'explanation': "dfsadfafafddsfafds",
                                'optionA': "testA",
                                'optionB': "testB",
                                'optionC': "testC",
                                'optionD': "testD",
                                'questionType': "1"
                            }
            }

            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url+'/cms-api/edu/question/add', data=payload1,headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200,'add')

        @allure.step("接口test_edu_question_getList")
        def test_edu_question_getList(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "page": {"pageNum": 1, "pageSize": 20},
                "content": {
                    "content": None
                }
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/edu/question/getList', data=payload1, headers=headers)
            global value
            value = r1.json()['content']['list'][0]['questionId']
            return (value)

        @allure.step("接口test_update")
        def test_update(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "content": {
                    'answer': "B",
                    'content': "test1222",
                    'explanation': "dfsadfafafddsfafds",
                    'optionA': "testA",
                    'optionB': "testB",
                    'optionC': "testC",
                    'optionD': "testD",
                    'questionType': "1",
                    'questionId':value
                }
            }

            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/edu/question/update', data=payload1, headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200, 'update')

        @allure.step("接口test_delete")
        def test_delete(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "content": {
                    'questionId': value
                }
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/edu/question/delete', data=payload1,
                               headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200, 'delete')


if __name__ == "__main__":
    pytest.main(['-s', 'test_add_edit_deletequestion'])
