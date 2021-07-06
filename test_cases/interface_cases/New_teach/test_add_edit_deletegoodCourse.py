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
        
        @allure.step("接口test_addRelationWithCourse")
        def test_addRelationWithCourse(self):
            payload1 = {
                'accessToken':config.TOKEN,
                'page': {'pageNum': 0, 'pageSize': 0},
                "content": {
                                'courseId': "118750559175053312"
                            }
            }

            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url+'/cms-api/edu/goodCourse/addRelationWithCourse', data=payload1,headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200,'addRelationWithCourse')

        @allure.step("接口test_selGoodCourseList")
        def test_selGoodCourseList(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "page": {"pageNum": 0, "pageSize": 20},
                "content": {

                    "title": ""
                }
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/edu/goodCourse/selGoodCourseList', data=payload1,
                               headers=headers)
            global value
            value = r1.json()['content']['list'][0]['goodCourseId']
            return (value)

        @allure.step("接口test_move")
        def test_move(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "content": {
                            'direction': "down",
                            'goodCourseId': value
                }
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/edu/goodCourse/move', data=payload1,
                               headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200, 'move')

        @allure.step("接口test_onOffRecommend")
        def test_onOffRecommend(self):
            payload1 = {
                'accessToken': config.TOKEN,
                'page': {'pageSize': 0, 'pageNum': 0},
                "content": {
                            'goodCourseId': value,
                            'onOff': "on"
                }
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/edu/goodCourse/onOffRecommend', data=payload1,
                               headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200, 'onOffRecommend')

        @allure.step("接口test_onOff")
        def test_onOff(self):
            payload1 = {
                'accessToken': config.TOKEN,
                'page': {'pageSize': 0, 'pageNum': 0},
                "content": {
                    'goodCourseId': value,
                    'onOff': "off"
                }
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/edu/goodCourse/onOff', data=payload1,
                               headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200, 'onOff')

        @allure.step("接口test_delete")
        def test_delete(self):
            payload1 = {
                'accessToken': config.TOKEN,
                'page': {'pageSize': 0, 'pageNum': 0},
                "content": {
                    'goodCourseId': value
                }
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/edu/goodCourse/delete', data=payload1,
                               headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200, 'delete')

if __name__ == "__main__":
    pytest.main(['-s', 'test_add_edit_deletegoodCourse'])
