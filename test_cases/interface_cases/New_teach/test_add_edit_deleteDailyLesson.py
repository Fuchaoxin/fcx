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
        
        @allure.step("接口test_addDailyLesson")
        def test_addDailyLesson(self):
            payload1 = {
                'accessToken':config.TOKEN,
                "content": {
                                'lessonTime': 1662076800000,
                                'videoId': "32197"
                            }
            }

            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url+'/cms-api/edu/dailyLesson/addDailyLesson', data=payload1,headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200,'addDailyLesson')

        @allure.step("接口test_dailyLessonList")
        def test_dailyLessonList(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "page": {"pageNum": 0, "pageSize": 999},
                "content": {
                    "endTime": 1664755199999,
                    "startTime": 1661731200000
                }
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/edu/dailyLesson/dailyLessonList', data=payload1,
                               headers=headers)
            global value
            print(r1.json())
            value = r1.json()['content'][0]['id']
            return (value)

        @allure.step("接口test_deleteDailyLesson")
        def test_deleteDailyLesson(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "content": {
                    'lessonId': value
                }
            }
            headers = {
                "Content-Type": "application/json"
            }
            print(value)
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/edu/dailyLesson/deleteDailyLesson', data=payload1,
                               headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200, 'deleteDailyLesson')


if __name__ == "__main__":
    pytest.main(['-s', 'test_add_edit_deleteDailyLesson'])
