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

@allure.step("接口test_addOrUpdateRankingData")
def test_addOrUpdateRankingData():
    payload1 = {
        'accessToken': config.TOKEN,
        "page": {"pageNum": 1, "pageSize": 20},
        "content": {
            'businessId': '203efab1-864e-41d2-a2f1-60ca3691d7d8',
            'failureTime': "2022-06-30 00:00:00",
            'id': "",
            'manualCount': "11",
            'type': "2"
                    }
    }
    headers = {
        "Content-Type": "application/json"
    }
    payload1 = json.dumps(payload1)
    r1 = requests.post(url=config.Pre_Url + '/cms-api/rankingTask/addOrUpdateRankingData', data=payload1,
                       headers=headers)
    As = AssertUtil()
    As.assert_code(r1.json()['code'], 10000, 'addOrUpdateRankingData')

if __name__ == "__main__":
    pytest.main(['-s', 'test_addOrUpdateRankingData'])
