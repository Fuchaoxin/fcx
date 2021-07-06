# -*- coding: utf-8 -*-
import requests
import pytest
import allure
from base import config
import json
from base.AssertUtil import AssertUtil
@allure.step("接口test_articleList")
@pytest.mark.parametrize("status,expect_result",[(None,200),(4,200),(5,200),(2,200),(3,200),(1,200)])
def test_articleList(status,expect_result):
    payload1 = {
        'accessToken':config.TOKEN,
        "page":{"pageNum": 1,"pageSize":20},
        "content": {"title": "",
                    "specialId": "",
                    "status": status
                    
                    }
    }
    headers = {
        "Content-Type": "application/json"
    }
    payload1 = json.dumps(payload1)
    r1 = requests.post(url=config.Pre_Url+'/ssax-cls-cms-api/article/list', data=payload1,headers=headers)
    As = AssertUtil()
    As.assert_code(r1.json()['code'], 200,'test_articleList')


if __name__ == "__main__":
    test_articleList()
    pytest.main(['-s','test_articleList.py'])
