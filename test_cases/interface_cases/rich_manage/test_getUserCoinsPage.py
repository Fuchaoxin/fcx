# -*- coding: utf-8 -*-
import requests
import pytest
import allure
from base import config
import json
from base.AssertUtil import AssertUtil
@allure.step("接口test_getUserCoinsPage")
def test_getUserCoinsPage():
    payload1 = {
        'accessToken':config.TOKEN,
        "page":{"pageNum": 1,"pageSize":20},
        "content": {

                    "phone": "",
                    "userId": "8b0bbeee-fe7a-4b3e-b630-0f479d1e99da"
                    }
    }
    headers = {
        "Content-Type": "application/json"
    }
    payload1 = json.dumps(payload1)
    r1 = requests.post(url=config.Pre_Url+'/shopping-cms-api/virtualCoin/getUserCoinsPage', data=payload1,headers=headers)
    As = AssertUtil()
    As.assert_code(r1.json()['code'], 200,'test_getUserCoinsPage')


if __name__ == "__main__":

    pytest.main(['-s','test_getUserCoinsPage.py'])
