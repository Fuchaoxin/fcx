# -*- coding: utf-8 -*-
import requests
import pytest
import allure
from base import config
import json
from base.AssertUtil import AssertUtil
@allure.step("接口test_articleList_select")
def test_articleList_select():
    payload1 = {
        'accessToken':config.TOKEN,
        "page":{"pageNum": 1,"pageSize":20},
        "content": {"title": "测试",
                    "specialId": 21,
                    "beginTime": "2021-02-01 00:00:00",
                    "endTime":"2021-06-21 23:59:59"
                    }
    }
    headers = {
        "Content-Type": "application/json"
    }
    payload1 = json.dumps(payload1)
    r1 = requests.post(url=config.Pre_Url+'/ssax-cls-cms-api/article/list', data=payload1,headers=headers)
    As = AssertUtil()
    As.assert_code(r1.json()['code'], 200,'test_articleList_select')

@allure.step("接口test_articleList_select_unpublish")
def test_articleList_select_unpublish():
    payload1 = {
        'accessToken':config.TOKEN,
        "page":{"pageNum": 1,"pageSize":20},
        "content": {"title": "测试",
                    "specialId": 21,
                    "status":4,
                    'unPublishStatus': 1,
                    'authorityValue': 1
                    }
    }
    headers = {
        "Content-Type": "application/json"
    }
    payload1 = json.dumps(payload1)
    r1 = requests.post(url=config.Pre_Url+'/ssax-cls-cms-api/article/list', data=payload1,headers=headers)
    As = AssertUtil()
    As.assert_code(r1.json()['code'], 200,'test_articleList_select_unpublish')

if __name__ == "__main__":
    pytest.main(['-s','test_articleList_select.py'])

