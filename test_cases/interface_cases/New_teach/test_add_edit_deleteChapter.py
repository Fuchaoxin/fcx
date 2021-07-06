# -*- coding: utf-8 -*-
import requests
import pytest
import allure
from base import config
import json
from base.AssertUtil import AssertUtil
import time
import random
import random
import random

class TestCase():
        value=1
        value1=1
        value2 = 1
        value3 = 1

        @allure.step("接口test_add")
        def test_add(self):
            payload1 = {
                'accessToken':config.TOKEN,
                "content": {
                                'chapterName': "123",
                                'direction': "after",
                                'imageUrl': "https://oss.caizidao.com.cn/rpdt/invest_educat/230-120.png",
                                'introduction': "212132132131232123",
                                'referenceChapterId': "117366423243853824",
                                'schoolId': "117295988217090048"
                            }
            }

            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            print(payload1)
            r1 = requests.post(url=config.Pre_Url+'/cms-api/edu/chapter/add', data=payload1,headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200,'add')

        @allure.step("接口test_getList")
        def test_getList(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "content": {'schoolName': "",
                            'schoolType': "A"
                            }
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/edu/school/getList', data=payload1,
                               headers=headers)
            global value3
            value3 = r1.json()['content'][0]['schoolId']
            return (value3)

        @allure.step("接口test_getListBySchoolId")
        def test_getListBySchoolId(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "content": {"chapterName": None,
                            "schoolId": value3
                            }
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/edu/chapter/getListBySchoolId', data=payload1,
                               headers=headers)
            global value
            value = r1.json()['content'][2]['chapterId']
            return (value)

        @allure.step("接口test_update")
        def test_update(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "content": {
                    'chapterId': value,
                    'chapterName': "12345",
                    'imageUrl': "https://oss.caizidao.com.cn/rpdt/invest_educat/230-120.png",
                    'introduction': "212132132131232123"
                }
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/edu/chapter/update', data=payload1,
                               headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200, 'update')

        @allure.step("接口test_relateVideo")
        def test_relateVideo(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "content": {
                    'chapterId': value,
                    'videoIds': ["32188"]
                }
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/edu/course/relateVideo', data=payload1,
                               headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200, 'relateVideo')

        @allure.step("接口test_getListByChapterId")
        def test_getListByChapterId(self):
            payload1 = {
                'accessToken': config.TOKEN,
                'page': {'pageNum': 1, 'pageSize': 20},
                "content": {
                    'chapterId': value,
                    'courseName': ""
                }
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/edu/course/getListByChapterId', data=payload1,
                               headers=headers)
            print(value)
            print(r1.json())
            global value1
            value1 = r1.json()['content']['list'][0]['courseId']
            return (value1)


        @allure.step("接口test_relateQuestion")
        def test_relateQuestion(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "content": {
                    'courseId': value1,
                    'questionIds': ["206074608481341440"]
                }
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/edu/courseExam/relateQuestion', data=payload1,
                               headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200, 'relateQuestion')

        @allure.step("接口test_getQuestionListByCourseId")
        def test_getQuestionListByCourseId(self):
            payload1 = {
                'accessToken': config.TOKEN,
                'page': {'pageNum': 1, 'pageSize': 20},
                "content": {
                    'courseId': value1,
                    'questionContent': ""
                }
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/edu/courseExam/getQuestionListByCourseId', data=payload1,
                               headers=headers)
            print(r1.json())
            global value2
            value2 = r1.json()['content']['list'][0]['questionId']
            return (value2)

        @allure.step("接口test_deleteQuestion")
        def test_deleteQuestion(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "content": {
                        'courseId': value1,
                        'questionId': value2
                }
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/edu/courseExam/deleteQuestion', data=payload1,
                               headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200, 'deleteQuestion')

        @allure.step("接口test_deleteCource")
        def test_deleteCource(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "content": {
                    'courseId': value1
                }
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/edu/course/delete', data=payload1,
                               headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200, 'deleteCource')

        @allure.step("接口test_deletechapter")
        def test_deletechapter(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "content": {
                    'chapterId': value
                }
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/edu/chapter/delete', data=payload1,
                               headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200, 'deletechapter')


if __name__ == "__main__":
    pytest.main(['-s', 'test_add_edit_deleteChapter'])
