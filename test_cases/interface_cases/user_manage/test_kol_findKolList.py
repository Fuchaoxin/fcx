# -*- coding: utf-8 -*-
import requests
import pytest
import allure
from base import config
import json
from base.AssertUtil import AssertUtil
@allure.step("接口test_kol_findKolList")
def test_kol_findKolList(test_getToken):
    payload1 = {
        'accessToken':test_getToken,
        "page":{"pageNum": 0,"pageSize":20},
        "content": {'creater': "",
                    'userId': ""
                    }
    }
    headers = {
        "Content-Type": "application/json"
    }
    payload1 = json.dumps(payload1)
    r1 = requests.post(url=config.Pre_Url+'/cms-api/kol/findKolList', data=payload1,headers=headers)
    As = AssertUtil()
    As.assert_code(r1.json()['code'], 200,'test_kol_findKolList')


if __name__ == "__main__":
    test_kol_findKolList()
    pytest.main(['-s','test_kol_findKolList.py'])
