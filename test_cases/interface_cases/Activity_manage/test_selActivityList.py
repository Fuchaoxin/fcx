# -*- coding: utf-8 -*-
import requests
import pytest
import allure
from base import config
import json
from base.AssertUtil import AssertUtil
@allure.step("接口test_selActivityList")
def test_selActivityList():
    payload1 = {
        "accessToken": config.TOKEN,
        "page":{"pageNum": 1,"pageSize":20},
        "content": {"activityName": ""}
    }
    headers ={
        "Content-Type":"application/json"
    }
    payload1 = json.dumps(payload1)
    r1 = requests.post(url=config.Pre_Url+'/shopping-cms-api/activity/selActivityList', data=payload1,headers=headers)
    As = AssertUtil()
    As.assert_code(r1.json()['code'], 200,'test_selActivityList')

if __name__ == "__main__":
    test_selActivityList()
    pytest.main(['-s','test_selActivityList.py'])
