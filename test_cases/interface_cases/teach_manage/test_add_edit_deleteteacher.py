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
        value1=1
        value2=1
      
        @allure.step("接口test_addUser")
        def test_addUser(self):
            payload1 = {
                'accessToken':config.TOKEN,
                "content": {
                                'appId': "8009d466f080410a9871ee829921094c",
                                'auditStatus': 0,
                                'creater': "白玲玉",
                                'imageUrl': "https://oss.caizidao.com.cn/rpdt/lecturer_head_image/1625041755392800X800.png",
                                'isDeleted': 0,
                                'isLecturer': 'true',
                                'jgtUserId': "88913463-81a0-40ed-b334-d7a9a41dc3cd",
                                'lecturerBannerImg': "https://oss.caizidao.com.cn/rpdt/lecturer_banner_image/1625041743390750X290.png",
                                'lecturerIntroduce': "212121222112122121",
                                'lecturerOneWords': "12212121",
                                'nickName': "test111"
                            }
            }

            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url+'/cms-api/teacher/addUser', data=payload1,headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200,'addUser')

        @allure.step("接口test_queryUserWithPage")
        def test_queryUserWithPage(self):
            payload1 = {
                'accessToken': config.TOKEN,
                'page': {'pageNum': 1, 'pageSize': 20},
                "content": {
                    'isDeleted': 0,
                    'isLecturer': 'true',
                    'nickName': None
                }
            }

            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/teacher/queryUserWithPage', data=payload1,
                               headers=headers)
            global value
            value = r1.json()['content']['list'][0]['lecturerId']
            return (value)

            global value1
            value1 = r1.json()['content']['list'][0]['appId']
            return (value1)
            global value2
            value2 = r1.json()['content']['list'][0]['userId']
            return (value2)

        @allure.step("接口test_move,down move")
        def test_move(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "page": {"pageNum": 0, "pageSize": 0},
                "content": {
                    'direction': "down",
                    'lecturerId': value
                            }
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/teacher/move', data=payload1,
                               headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200, 'move-down')

        @allure.step("接口test_move,up move")
        def test_move1(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "page": {"pageNum": 0, "pageSize": 0},
                "content": {
                    'direction': "up",
                    'lecturerId': value
                }
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/teacher/move', data=payload1,
                               headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200, 'move-up')

        @allure.step("接口test_onOffRecommend")
        def test_onOffRecommend(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "page": {"pageNum": 0, "pageSize": 0},
                "content": {
                    'lecturerId': value,
                    'onOff': "on"
                }
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/teacher/onOffRecommend', data=payload1,
                               headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200, 'onOffRecommend')

        @allure.step("接口test_queryUserWithPage1")
        def test_queryUserWithPage1(self):
            payload1 = {
                'accessToken': config.TOKEN,
                'page': {'pageNum': 1, 'pageSize': 20},
                "content": {
                    'isDeleted': 0,
                    'isLecturer': 'true',
                    'nickName': None
                }
            }

            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/teacher/queryUserWithPage', data=payload1,
                               headers=headers)

            global value1
            value1 = r1.json()['content']['list'][0]['appId']
            return (value1)

        @allure.step("接口test_queryUserWithPage2")
        def test_queryUserWithPage2(self):
            payload1 = {
                'accessToken': config.TOKEN,
                'page': {'pageNum': 1, 'pageSize': 20},
                "content": {
                    'isDeleted': 0,
                    'isLecturer': 'true',
                    'nickName': None
                }
            }

            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/teacher/queryUserWithPage', data=payload1,
                               headers=headers)
            global value2
            value2 = r1.json()['content']['list'][0]['userId']
            return (value2)

        @allure.step("接口test_modUser")
        def test_modUser(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "content": {
                    'appId': value1,
                    'isDeleted': 1,
                    'userId': value2

                }
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/teacher/modUser', data=payload1,
                               headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200, 'modUser')


if __name__ == "__main__":
    pytest.main(['-s', 'test_add_edit_deleteteacher'])
