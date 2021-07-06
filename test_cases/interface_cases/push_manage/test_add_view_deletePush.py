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
#@pytest.mark.usefixture("test_getToken")
class TestCase():
        value=1
      
        @allure.step("接口test_sendJob")
        def test_sendJob(self):
            payload1 = {
                        'accessToken':config.TOKEN,
                        'send': {
                        'activityType': "0504",
                        'appId': "cms",
                        'createTime': '1624351277428',
                        'cron': "00 00 00 01 06 ? 2022",
                        'defineTime': '1654012800000',
                        'enable': 1,
                        'linkId': "",
                        'linkType': None,
                        'modifyTime': '1654012800000',
                        'name': "",
                        'operator': "白玲玉",
                        'sendTags': [
                        {
                        'dom': "",
                        'h5Url': "",
                        'linkAddress': "",
                        'targetAddress': "",
                        'targetParams': {},
                        'targetTab': 1,
                        'type': "3",
                        'views': {
                        'btnTitle': "",
                        'content': "https://oss.caizidao.com.cn/rpdt/pushMaterial/710.png",
                        'imageUrl': "https://oss.caizidao.com.cn/pushSystem/rpdt/push/appPush/162435123545572.png",
                        'materialType': 1,
                        'pageName': "",
                        'preImg': "",
                        'subTitle': "11111111111111111111",
                        'title': "11111111111111111111",
                        'titleContent': "11111111111111111111111111111111111111111111111111"}}],
                        'status': 1,
                        'targetUserType': 1,
                        'targetUsers': None,
                        'uid': "MO1PUSH967088040"
                    }
            }

            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url+'/cms-api/template/sendJob', data=payload1,headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200,'sendJob')

        @allure.step("接口test_getJobs")
        def test_getJobs(self):
            payload1 = {
                'accessToken': config.TOKEN,
                'appId': "cms",
                'enable': 1,
                'operator': "",
                'pageNum': 1,
                'pageSize': 20,
                'status': None,
                'tagType': None,
                'targetUser': [],
                'uid': None
            }
            headers = {
                "Content-Type": "application/json",
                "Authorization": "false"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/template/getJobs', data=payload1, headers=headers)
            global value
            value= r1.json()['content']['list'][0]['appSid']
            print(value)
            return(value)

        @allure.step("接口test_switchJob")
        def test_switchJob(self):
            payload1 = {
                'accessToken': config.TOKEN,
                'id': value,
                'status': 0

            }

            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/template/switchJob', data=payload1, headers=headers)

            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200, 'switchJob')


        @allure.step("接口test_delJob")
        def test_delJob(self):
                payload1 = {
                            'accessToken': config.TOKEN,
                            'id': value,
                            'enable': 0

                }
                headers = {
                            "Content-Type": "application/json"
                            }
                payload1 = json.dumps(payload1)
                r1 = requests.post(url=config.Pre_Url + '/cms-api/template/delJob', data=payload1,
                               headers=headers)
                As = AssertUtil()
                As.assert_code(r1.json()['code'], 200, 'delJob')

if __name__ == "__main__":
    pytest.main(['-s', 'test_add_view_deletePush'])
