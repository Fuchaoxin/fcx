# -*- coding: utf-8 -*-
import requests
import pytest
import allure
from base import config
import json
from base.AssertUtil import AssertUtil
@allure.step("接口test_suggestTopicList")
def test_suggestTopicList(test_getToken):
    payload1 = {
        'accessToken':test_getToken,
        'content': {'type': "app"}
    }
    headers = {
        "Content-Type": "application/json"
    }
    payload1 = json.dumps(payload1)
    r1 = requests.post(url=config.Pre_Url+'/shopping-cms-api//creator/suggestTopicList', data=payload1,headers=headers)
    As = AssertUtil()
    As.assert_code(r1.json()['code'], 200,'test_suggestTopicList')


if __name__ == "__main__":
    test_suggestTopicList()
    pytest.main(['-s','test_suggestTopicList.py'])
