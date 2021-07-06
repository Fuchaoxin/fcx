# -*- coding: utf-8 -*-
import requests
import pytest
import allure
from base import config
import json
from base.AssertUtil import AssertUtil
@allure.step("接口test_wealth_getDetailByLevelId")
def test_wealth_getDetailByLevelId():
    payload1 = {
        "accessToken": config.TOKEN,
        'content':{
            'levelId': "1"
        }

    }
    headers ={
        "Content-Type":"application/json"
    }
    payload1 = json.dumps(payload1)
    r1 = requests.post(url=config.Pre_Url+'/shopping-cms-api/wealth/getDetailByLevelId', data=payload1,headers=headers)
    As = AssertUtil()
    As.assert_code(r1.json()['code'], 200,'test_wealth_getDetailByLevelId')


if __name__ == "__main__":
    test_wealth_getDetailByLevelId()
    pytest.main(['-s','test_wealth_getDetailByLevelId.py'])
