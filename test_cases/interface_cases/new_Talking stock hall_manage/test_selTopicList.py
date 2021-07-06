# -*- coding: utf-8 -*-
import requests
import pytest
import allure
from base import config
import json
from base.AssertUtil import AssertUtil
@allure.step("接口test_selTopicList")
def test_selTopicList():
    payload1 = {
        'accessToken':config.TOKEN,
        "page":{"pageNum": 1,"pageSize":20},
        "content": {
            'dimensionTime': 1622624104977,
            'endTime': "",
            'isTop': "",
            'sort': "",
            'startTime': "",
            'topicName': ""
        }
    }
    headers = {
        "Content-Type": "application/json"
    }
    payload1 = json.dumps(payload1)
    r1 = requests.post(url=config.Pre_Url+'/cms-api/topicTask/selTopicList', data=payload1,headers=headers)
    As = AssertUtil()
    As.assert_code(r1.json()['code'], 200,'test_selTopicList')



if __name__ == "__main__":
    test_selTopicList()
    pytest.main(['-s','test_selTopicList.py'])
