# -*- coding: utf-8 -*-
import requests
import pytest
import allure

@allure.step("接口test_getUserInfo")
def test_getUserInfo(test_getToken):
    payload1 = {
        'accessToken':test_getToken
    }
    headers = {
        "Content-Type": "application/json"
    }
    print("UserInfo_test_getToken: ")
    print(test_getToken)
    r1 = requests.post(url='https://rpdtssax-cms.caizidao.com.cn:9011/cms-api/staff/getUserInfo', params=payload1,headers=headers)
    if r1.status_code != 200 :
        print("\ngetUserInfo failed!!!!!!")
    else:
        print("\ngetUserInfo Pass!!!!!!")


if __name__ == "__main__":
    test_getUserInfo()
    pytest.main(['-s','test_getUserInfo.py'])
