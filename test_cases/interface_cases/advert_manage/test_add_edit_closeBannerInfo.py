# -*- coding: utf-8 -*-
import requests
import pytest
import allure
from base import config
import json
from base.AssertUtil import AssertUtil
from test_cases.interface_cases import conftest
import time
import random
import random
import random
#@pytest.mark.usefixture("config.TOKEN")
class TestCase():
        value=1

        @allure.step("接口test_addBannerInfo")
        def test_addBannerInfo(self):
            payload1 = {
                'accessToken':config.TOKEN,
                "content": {
                                'adBannerName': "test轮播图",
                                'appType': "2",
                                'endShowTime': 1719331200000,
                                'materialCode': "PIC234239674447876096",
                                'materialSonId': 1382,
                                'oneLevel': "A",
                                'onePcLevel': "A",
                                'oneSmallLevel': "",
                                'pushUserCity': [],
                                'pushUserRegisterTime': None,
                                'pushUserSex': [],
                                'pushUserStockAge': [],
                                'pushUserUlabelId': [],
                                'startShowTime': 1624291200000,
                                'targetUserType': "1",
                                'twoLevel': ""
                            }
            }

            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url+'/cms-api/adBanner/addBannerInfo', data=payload1,headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200,'addBannerInfo')

        @allure.step("接口test_selAdBannerList")
        def test_selAdBannerList(self):
            payload1 = {
                "accessToken": config.TOKEN,
                "page": {"pageNum": 1, "pageSize": 20},
                "content": {"adBannerName": None,
                            "adBannerStatus": 0,
                            "appType": "",
                            "creator": None,
                            "endCreateTime": None,
                            "oneLevel": "",
                            "startCreateTime": None,
                            "twoLevelName": ""}
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/adBanner/selAdBannerList', data=payload1, headers=headers)
            global value
            value = r1.json()['content']['list'][0]['adBannerId']
            return (value)

        @allure.step("接口test_updateBannerInfo")
        def test_updateBannerInfo(self):
            payload1 = {
                'accessToken':config.TOKEN,
                "content": {
                                'adBannerName': "test轮播图"+str(random.randint(1,9999)),
                                'appType': "2",
                                'endShowTime': 1719331200000,
                                'materialCode': "PIC234239674447876096",
                                'materialSonId': 1382,
                                'oneLevel': "A",
                                'onePcLevel': "A",
                                'adBannerId':value,
                                'pushUserCity': [],
                                'pushUserRegisterTime': None,
                                'pushUserSex': [],
                                'pushUserStockAge': [],
                                'pushUserUlabelId': [],
                                'startShowTime': 1624291200000,
                                'targetUserType': "1",
                                'twoLevel': ""
                            }
            }
            print(payload1)
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url+'/cms-api/adBanner/updateBannerInfo', data=payload1,headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200,'updateBannerInfo')

        @allure.step("接口test_useAdBannerById")
        def test_useAdBannerById(self):
            payload1 = {
                'accessToken':config.TOKEN,
                "content": {'adBannerId':value}
            }

            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url+'/cms-api/adBanner/useAdBannerById', data=payload1,headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200,'useAdBannerById')


if __name__ == "__main__":
    pytest.main(['-s', 'test_add_edit_closeBannerInfo'])
