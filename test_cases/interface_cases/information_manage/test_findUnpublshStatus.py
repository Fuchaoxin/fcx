# -*- coding: utf-8 -*-
import requests
import pytest
import allure
from base import config
import json
from base.AssertUtil import AssertUtil
@allure.step("接口test_findUnpublshStatus")
def test_findUnpublshStatus(test_getToken):
    payload1 = {
        'accessToken':test_getToken,
        "content": {}
    }
    headers = {
        "Content-Type": "application/json"
    }
    payload1 = json.dumps(payload1)
    r1 = requests.post(url=config.Pre_Url+'/ssax-cls-cms-api/article/findUnpublshStatus', data=payload1,headers=headers)
    As = AssertUtil()
    As.assert_code(r1.json()['code'], 200,'test_findUnpublshStatus')


if __name__ == "__main__":
    test_findUnpublshStatus()
    pytest.main(['-s','test_findUnpublshStatus.py'])
