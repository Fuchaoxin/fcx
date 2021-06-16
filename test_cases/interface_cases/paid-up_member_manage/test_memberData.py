# -*- coding: utf-8 -*-
import requests
import pytest
import allure
from base import config
import json
from base.AssertUtil import AssertUtil

#@allure.step("接口test_memberData")
@pytest.mark.parametrize("content,expect_result",[(1000003,200),(1000004,200),(1000005,200)])
def test_memberData(test_getToken,content,expect_result):
    payload1 = {
        'accessToken':test_getToken,
        'content': content
    }
    headers = {
        "Content-Type": "application/json"
    }
    payload1 = json.dumps(payload1)
    r1 = requests.post(url=config.Pre_Url+'/shopping-cms-api/member/ui/data', data=payload1,headers=headers)

    As = AssertUtil()
    As.assert_code(r1.json()['code'],expect_result,'test_memberData')

if __name__ == "__main__":
    #test_memberData(1000004)
    pytest.main(['-s','test_memberData.py'])
