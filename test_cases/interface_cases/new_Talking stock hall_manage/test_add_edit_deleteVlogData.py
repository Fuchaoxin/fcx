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
        value1=1
        @allure.step("接口test_getUploadVideoAddressAuth")
        def test_getUploadVideoAddressAuth(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "page": {"pageNum": 1, "pageSize": 20},
                "content": {
                            'fileName': "1.mp4",
                            'title': "11111"
                }
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/vodUploadAuth/getUploadVideoAddressAuth', data=payload1, headers=headers)
            global value1
            value1 = r1.json()['content']['videoId']
            return (value1)

        @allure.step("接口test_addVlogData")
        def test_addVlogData(self):
            payload1 = {
                'accessToken':config.TOKEN,
                'page': {'pageNum': 1, 'pageSize': 20},
                "content": {
                                'account': None,
                                'aliUploadList': [{
                                'beginTime': None,
                                'endTime': None,
                                'theTIme': None,
                                'uploadAddress': "",
                                'uploadAuth': ""}],
                                'appNoticeStatus': None,
                                'appNoticeTime': None,
                                'beginTime': None,
                                'commentCount': None,
                                'createTime': None,
                                'description': None,
                                'endTime': None,
                                'examineStatus': None,
                                'fileName': "1.mp4",
                                'followCount': None,
                                'id': None,
                                'jgmVideoSetList': [],
                                'labelName': "",
                                'labelVOList': [],
                                'mediaType': "Video",
                                'popImage': None,
                                'popVideoSet': "{\"videoSetId\":12393,\"videoSetName\":\"测试11\"}",
                                'positionDescription': None,
                                'privacy': "1",
                                'publishStatus': None,
                                'publishTime': 1628554903000,
                                'replies': None,
                                'rightsRuleVideo': {
                                                    'isNomemberPay': "",
                                                    'isPayPrice': "",
                                                    'isTrySee': "",
                                                    'nomemberPrice': "",
                                                    'trySeeTime': ""},
                                'setId': "195",
                                'smallCoverHeigh': None,
                                'smallCoverUrl': None,
                                'smallCoverWidth': None,
                                'sortNum': None,
                                'title': "test123",
                                'uploadImageUrl': None,
                                'uploadInfoVOS': [],
                                'userId': "0815c4c9-d45b-427e-8742-b0dae5974546",
                                'videoId': value1
                            }
            }

            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url+'/cms-api/v2/vlogTask/addVlogData', data=payload1,headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200,'addVlogData')

        @allure.step("接口test_selVlogList")
        def test_selVlogList(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "page": {"pageNum": 1, "pageSize": 20},
                "content": {
                    'account': None,
                    'beginTime': None,
                    'endTime': None,
                    'examineStatus': None,
                    'labelVOList': None,
                    'mediaType': None,
                    'payStatus': None,
                    'title': None,
                    'topic': "",
                    'words': None
                }
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/vlogTask/selVlogList', data=payload1, headers=headers)
            global value
            value = r1.json()['content']['list'][0]['id']
            return (value)

        @allure.step("接口test_delVlogData")
        def test_delVlogData(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "page": {"pageNum": 1, "pageSize": 20},
                "content": {
                    'ids':[value]
                }
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/v2/vlogTask/delVlogData', data=payload1, headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200, 'test_delVlogData')

if __name__ == "__main__":
    pytest.main(['-s', 'test_add_edit_deleteVlogData'])
