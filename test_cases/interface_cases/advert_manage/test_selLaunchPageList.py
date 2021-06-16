# -*- coding: utf-8 -*-
import requests
import pytest
import allure
from base import config
import json
from base.AssertUtil import AssertUtil
@allure.step("接口test_selLaunchPageList")
def test_selLaunchPageList(test_getToken):
    payload1 = {
        "accessToken": test_getToken,
        "page":{"pageNum": 1,"pageSize":20},
        "content": {"creator": None,
                    "endCreateTime": None,
                    "launchPageName": None,
                    "launchPageStatus": 0,
                    "startCreateTime": None}
    }
    headers ={
        "Content-Type":"application/json"
    }
    payload1 = json.dumps(payload1)
    r1 = requests.post(url=config.Pre_Url+'/cms-api/launchPage/selLaunchPageList', data=payload1,headers=headers)
    As = AssertUtil()
    As.assert_code(r1.json()['code'], 200,'test_selLaunchPageList')


if __name__ == "__main__":
    test_selLaunchPageList()
    pytest.main(['-s','test_selLaunchPageList.py'])
