# -*- coding: utf-8 -*-
import requests
import pytest
import allure
from base import config
import json
from base.AssertUtil import AssertUtil
@allure.step("接口test_queryVideoSetCategories")
def test_queryVideoSetCategories():
    payload1 = {
        'accessToken':config.TOKEN,
        "page":{"pageNum": 0,"pageSize":0},
        "content": {
                    'expand': 'false',
                    'parentId': 0
                    }
    }
    headers = {
        "Content-Type": "application/json"
    }
    payload1 = json.dumps(payload1)
    r1 = requests.post(url=config.Pre_Url+'/cms-api/cms/videoset/category/queryVideoSetCategories', data=payload1,headers=headers)
    As = AssertUtil()
    As.assert_code(r1.json()['code'], 200,'test_queryVideoSetCategories')

if __name__ == "__main__":

    pytest.main(['-s','test_queryVideoSetCategories.py'])
