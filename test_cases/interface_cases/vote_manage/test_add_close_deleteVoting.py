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

        @allure.step("接口test_addVotingData")
        def test_addVotingData(self):
            payload1 = {
                'accessToken':config.TOKEN,
                "page":{"pageNum": 1,"pageSize":20},
                "content": {'endTime': "2030-06-01 00:00:00",
                            'optionsList': ["123","456"],
                            'source': "1",
                            'startTime': "2021-06-01 00:00:00",
                            'userType': 1,
                            'voteMore': "1",
                            'votingBatchId': "",
                            'votingThemeName': "1233"
                            }
            }

            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url+'/shopping-cms-api/voting/addVotingData', data=payload1,headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200,'test_addVotingData')

        @allure.step("接口test_selVotingDataList")
        def test_selVotingDataList(self):
            payload1 = {
                'accessToken':config.TOKEN,
                "page":{"pageNum": 1,"pageSize":20},
                "content": {"voteSate": "",
                            "votingThemeName": "1233"
                            }
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url+'/shopping-cms-api/voting/selVotingDataList', data=payload1,headers=headers)
            As = AssertUtil()
            return(r1.json()['content']['list'][0]['votingBatchId'])
            #As.assert_code(r1.json()['code'], 200,'test_selVotingDataList')

        @allure.step("接口test_closeVotingData")
        def test_closeVotingData(self):
            payload1 = {
                'accessToken':config.TOKEN,
                "content": [self.test_selVotingDataList()]
            }
            print(payload1)
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url+'/shopping-cms-api/voting/closeVotingData', data=payload1,headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200,'test_closeVotingData')

        @allure.step("接口test_delVotingData")
        def test_delVotingData(self):
            payload1 = {
                'accessToken':config.TOKEN,
                "content": [self.test_selVotingDataList()]
            }

            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url+'/shopping-cms-api/voting/delVotingData', data=payload1,headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200,'delVotingData')


if __name__ == "__main__":
    pytest.main(['-s', 'test_add_close_deleteVoting'])
