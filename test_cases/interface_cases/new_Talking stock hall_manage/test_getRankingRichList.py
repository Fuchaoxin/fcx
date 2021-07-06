# -*- coding: utf-8 -*-
import requests
import pytest
import allure
from base import config
import json
from base.AssertUtil import AssertUtil
@allure.step("接口test_getRankingRichList")
def test_getRankingRichList():
    payload1 = {
        'accessToken':config.TOKEN,
        "page":{"pageNum": 1,"pageSize":10},
        "content": {
             'topicName': ""
        }
    }
    headers = {
        "Content-Type": "application/json"
    }
    payload1 = json.dumps(payload1)
    r1 = requests.post(url=config.Pre_Url+'/cms-api/rankingTask/getRankingRichList', data=payload1,headers=headers)
    As = AssertUtil()
    As.assert_code(r1.json()['code'], 200,'test_getRankingRichList')


if __name__ == "__main__":
    test_getRankingRichList()
    pytest.main(['-s','test_getRankingRichList.py'])
