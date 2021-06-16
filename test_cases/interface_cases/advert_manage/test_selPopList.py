# -*- coding: utf-8 -*-
import requests
import pytest
import allure
from base import config
import json
from base.AssertUtil import AssertUtil
@allure.step("接口test_selPopList")
def test_selPopList(test_getToken):
    payload1 = {
        "accessToken": test_getToken,
        "page":{"pageNum": 1,"pageSize":20},
        "content": {"appType": "",
                    "creator": None,
                    "endCreateTime": None,
                    "popName": None,
                    "popStatus": 0,
                    "popType": 0,
                    "startCreateTime": None}
    }
    headers ={
        "Content-Type":"application/json"
    }
    payload1 = json.dumps(payload1)
    r1 = requests.post(url=config.Pre_Url+'/cms-api/pop/selPopList', data=payload1,headers=headers)
    As = AssertUtil()
    As.assert_code(r1.json()['code'], 200,'test_selPopList')


if __name__ == "__main__":
    test_selPopList()
    pytest.main(['-s','test_selPopList.py'])
