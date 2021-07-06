# -*- coding: utf-8 -*-
import requests
import pytest
import allure
from base import config
import json
from base.AssertUtil import AssertUtil
@allure.step("接口test_selChosedRecommendUsers")
def test_selChosedRecommendUsers():
    payload1 = {
        "accessToken": config.TOKEN

    }
    headers ={
        "Content-Type":"application/json"
    }
    payload1 = json.dumps(payload1)
    r1 = requests.post(url=config.Pre_Url+'/cms-api/vlogTask/selChosedRecommendUsers', data=payload1,headers=headers)
    As = AssertUtil()
    As.assert_code(r1.json()['code'], 200,'test_selChosedRecommendUsers')


if __name__ == "__main__":
    test_selChosedRecommendUsers()
    pytest.main(['-s','test_selChosedRecommendUsers.py'])
