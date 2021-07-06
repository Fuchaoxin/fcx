# -*- coding: utf-8 -*-
import requests
import pytest
import allure
from base import config
import json
from base.AssertUtil import AssertUtil
@allure.step("接口test_selTopicPlacedSort")
def test_selTopicPlacedSort():
    payload1 = {
        'accessToken':config.TOKEN,
        "page":{"pageNum": 1,"pageSize":20}

    }
    headers = {
        "Content-Type": "application/json"
    }
    payload1 = json.dumps(payload1)
    r1 = requests.post(url=config.Pre_Url+'/cms-api/topicTask/selTopicPlacedSort', data=payload1,headers=headers)
    As = AssertUtil()
    As.assert_code(r1.json()['code'], 200,'test_selTopicPlacedSort')


if __name__ == "__main__":
    pytest.main(['-s','test_selTopicPlacedSort.py'])
