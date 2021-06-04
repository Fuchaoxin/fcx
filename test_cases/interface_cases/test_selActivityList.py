# -*- coding: utf-8 -*-
import requests
import pytest
import allure

@allure.step("接口test_selActivityList")
def test_selActivityList(test_getToken):
    payload1 = {
        "accessToken": test_getToken,
        "page":{"pageNum": 1,"pageSize":20},
        "content": {"activityName": ""}
    }
    headers ={
        "Content-Type":"application/json"
    }
    print("sel_test_getToken: ")
    print(test_getToken)
    r1 = requests.post(url='https://rpdtssax-cms.caizidao.com.cn:9011/shopping-cms-api/activity/selActivityList', params=payload1,headers=headers)
    if r1.status_code != 200:
        print("\nselActivityList failed!!!!!!")
    else:
        print("\nselActivityList Pass!!!!!!")


if __name__ == "__main__":
    test_selActivityList()
    pytest.main(['-s','test_selActivityList.py'])
