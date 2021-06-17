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

       # @pytest.fixture(scope='module')
        def test_getToken(self):
            Token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJleHAiOjE2MjM5MTYzMDEsImlhdCI6MTYyMzkxNDUwMSwianRpIjoiOWJhODc0MTkzMjQwNDUxOTg1NjQ5ZTc1NmU3Y2EzMDYiLCJzdWIiOiJiYWlsaW5neXUifQ.Ngl-DWVMLaaSKdr7csQQCJ3ceLRQ4ghdRe7FMGAvZ2QnvfAAHYR6-1HfIXXKTlNqOGa0egAWiatA2xthhJp_Rvm4zQ1fF9feQkN4O1rIqHGKfo_GY_jhVmLsTcCppqp1EqmyGzqtp2d8UxpeWJ5Rrsqzn7zoZ42jeNVGa20wRKgqHu0YHJEG3AY0Ly9TNB0SpljNGDA-2xJ0oWdWQJR7OatoBfxT30IMIQW8rudn8mYavf63M6JYaWmG5vIgyWbTU2hnt3z9eA7U-tj9U-bUfgrx7uRFYQUZpwwtjZnBOTBL_EMrDFmbOz3TPV6l9rpMCPoUPCr7piSE8U1GCXj0Qg'
            return Token

        @allure.step("接口test_addVotingData")
        def test_addVotingData(self):
            payload1 = {
                'accessToken':self.test_getToken(),
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
                'accessToken':self.test_getToken(),
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
                'accessToken':self.test_getToken(),
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
                'accessToken':self.test_getToken(),
                "content": [self.test_selVotingDataList()]
            }
            print(payload1)
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url+'/shopping-cms-api/voting/delVotingData', data=payload1,headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200,'delVotingData')


if __name__ == "__main__":
    pytest.main(['-s', 'test_add_close_deleteVoting'])
