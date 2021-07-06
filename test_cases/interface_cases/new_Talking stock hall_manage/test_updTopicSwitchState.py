# -*- coding: utf-8 -*-
import requests
import pytest
import allure
from base import config
import json
from base.AssertUtil import AssertUtil

@allure.step("接口test_updTopicSwitchState")
@pytest.mark.parametrize("switchState,expect_result",[(1,200),(0,200)])
def test_updTopicSwitchState(switchState,expect_result):
    payload1 = {
        'accessToken':config.TOKEN,
        'page': {'pageNum': 1, 'pageSize': 20},
        'content': {
                        'id': 3,
                        'switchState': switchState,
                        'type': "1"
        }
    }
    headers = {
        "Content-Type": "application/json"
    }
    payload1 = json.dumps(payload1)
    r1 = requests.post(url=config.Pre_Url+'/cms-api/topicTask/updTopicSwitchState', data=payload1,headers=headers)

    As = AssertUtil()
    As.assert_code(r1.json()['code'],expect_result,'test_updTopicSwitchState')

if __name__ == "__main__":
    pytest.main(['-s','test_updTopicSwitchState.py'])
