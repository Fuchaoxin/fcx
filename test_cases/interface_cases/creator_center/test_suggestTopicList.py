# -*- coding: utf-8 -*-
import requests
import pytest
import allure
from base import config
import json
from base.AssertUtil import AssertUtil
@allure.step("接口test_suggestTopicList")
@pytest.mark.parametrize("type,expect_result",[("app",200),("pc",200)])
def test_suggestTopicList(type,expect_result):
    payload1 = {
        'accessToken':config.TOKEN,
        'content': {'type': type}
    }
    headers = {
        "Content-Type": "application/json"
    }
    payload1 = json.dumps(payload1)
    r1 = requests.post(url=config.Pre_Url+'/shopping-cms-api//creator/suggestTopicList', data=payload1,headers=headers)
    As = AssertUtil()
    As.assert_code(r1.json()['code'], 200,'test_suggestTopicList')


if __name__ == "__main__":

    pytest.main(['-s','test_suggestTopicList.py'])
