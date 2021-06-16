# -*- coding: utf-8 -*-
import requests
import pytest
import allure
from base import config
import json
from base.AssertUtil import AssertUtil
@allure.step("接口test_selAdBannerList")
def test_selAdBannerList(test_getToken):
    payload1 = {
        "accessToken": test_getToken,
        "page":{"pageNum": 1,"pageSize":20},
        "content": {"adBannerName": None,
                    "adBannerStatus": 0,
                    "appType": "",
                    "creator": None,
                    "endCreateTime": None,
                    "oneLevel": "",
                    "startCreateTime": None,
                    "twoLevelName": ""}
    }
    headers ={
        "Content-Type":"application/json"
    }
    payload1 = json.dumps(payload1)
    r1 = requests.post(url=config.Pre_Url+'/cms-api/adBanner/selAdBannerList', data=payload1,headers=headers)
    As = AssertUtil()
    As.assert_code(r1.json()['code'], 200,'test_selAdBannerList')


if __name__ == "__main__":
    test_selAdBannerList()
    pytest.main(['-s','test_selAdBannerList.py'])
