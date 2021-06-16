# -*- coding: utf-8 -*-
import requests
import pytest
import allure
from base import config
import json
from base.AssertUtil import AssertUtil
@allure.step("接口test_labour_findLabourList")
def test_labour_findLabourList(test_getToken):
    payload1 = {
        'accessToken':test_getToken,
        "page":{"pageNum": 0,"pageSize":20},
        "content": {'creater': ""
                    }
    }
    headers = {
        "Content-Type": "application/json"
    }
    payload1 = json.dumps(payload1)
    r1 = requests.post(url=config.Pre_Url+'/cms-api/labour/findLabourList', data=payload1,headers=headers)
    As = AssertUtil()
    As.assert_code(r1.json()['code'], 200,'test_labour_findLabourList')

if __name__ == "__main__":
    test_labour_findLabourList()
    pytest.main(['-s','test_labour_findLabourList.py'])