# -*- coding: utf-8 -*-
import requests
import pytest
import allure
from base import config
import json
from base.AssertUtil import AssertUtil
import random

@allure.step("接口test_delVirmediaHotSort")
def test_delVirmediaHotSort():
    payload1 = {
        'accessToken':config.TOKEN,
        'id': "171",
        'mediaSort': 3,
        'virMediaId': "e3c243a0-fbc9-4150-8ae0-9e032a17fa78"
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization":"false"
    }
    payload1 = json.dumps(payload1)
    r1 = requests.post(url=config.Pre_Url+'/cms-api/virmediaHotSort/delVirmediaHotSort', data=payload1,headers=headers)
    As = AssertUtil()
    As.assert_code(r1.json()['code'], 200,'test_delVirmediaHotSort')

if __name__ == "__main__":

    pytest.main(['-s','test_delVirmediaHotSort.py'])
