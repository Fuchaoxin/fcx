# -*- coding: utf-8 -*-
import requests
import pytest
import allure
from base import config
import json
from base.AssertUtil import AssertUtil
@allure.step("接口test_virmediaIntervalNumList")
def test_virmediaIntervalNumList():
    payload1 = {
        'accessToken':config.TOKEN,
        "page":{"pageNum": 1,"pageSize":20},
        "content": {
            'checkStatus': "1",
            'mediaStatus': "1",
            'privacy': None,
            'pro': None,
            'state': None,
            'title': ""
                    }
    }
    headers = {
        "Content-Type": "application/json"
    }
    payload1 = json.dumps(payload1)
    r1 = requests.post(url=config.Pre_Url+'/cms-api/virmediaHotSort/virmediaIntervalNumList', data=payload1,headers=headers)
    As = AssertUtil()
    As.assert_code(r1.json()['code'], 200,'test_virmediaIntervalNumList')


if __name__ == "__main__":

    pytest.main(['-s','test_virmediaIntervalNumList.py'])
