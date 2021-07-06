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
        
        @allure.step("接口test_addEduVideo")
        def test_addEduVideo(self):
            payload1 = {
                'accessToken':config.TOKEN,
                "content": {
                                'aliVideoId': "1223ea4dc1f34bf085f37f5f66c9516a",
                                'coverImg': "https://rpdt-czd-vod.1shitou.cn/image/cover/96D473FF1A52426B833723195A6F8AA8-6-2.png?auth_key=1719815492-0-0-cd2ed85279807076855009cee1b47f5d",
                                'duration': 1.112,
                                'introduce': [{'title': None,
                                                'content': "111111111111111111111111111111111111111111111111111111111111111111111111"}],
                                'keywords': None,
                                'lectureId': "30e731a3-1eaa-4a7b-a477-958e7120425a",
                                'source': "1",
                                'title': "test1111111",
                                'videoNature': "B"
                            }
            }

            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url+'/cms-api/edu/video/addEduVideo', data=payload1,headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200,'addEduVideo')

        @allure.step("接口test_listEduVideo")
        def test_listEduVideo(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "page": {"pageNum": 1, "pageSize": 20},
                "content": {
                    "title": ""
                }
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/edu/video/listEduVideo', data=payload1, headers=headers)
            global value
            value = r1.json()['content']['list'][0]['id']
            return (value)

        @allure.step("接口test_updateEduVideo")
        def test_updateEduVideo(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "content": {
                    'aliVideoId': "1223ea4dc1f34bf085f37f5f66c9516a",
                    'coverImg': "https://rpdt-czd-vod.1shitou.cn/image/cover/96D473FF1A52426B833723195A6F8AA8-6-2.png?auth_key=1719815492-0-0-cd2ed85279807076855009cee1b47f5d",
                    'duration': 1.112,
                    'introduce': [{'title': None,
                                   'content': "111111111111111111111111111111111111111111111111111111111111111111111111"}],
                    'id': value,
                    'lectureId': "cc1cfc85-9b9d-4fa2-ac64-595a418589fd",
                    'source': "1",
                    'title': "test1111111",
                    'videoNature': "B"
                }
            }

            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/edu/video/updateEduVideo', data=payload1, headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200, 'updateEduVideo')

        @allure.step("接口test_deleteEduVideo")
        def test_deleteEduVideo(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "content": {
                    'id': value
                }
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/edu/video/deleteEduVideo', data=payload1,
                               headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200, 'deleteEduVideo')


if __name__ == "__main__":
    pytest.main(['-s', 'test_add_edit_deleteEduVideo'])
