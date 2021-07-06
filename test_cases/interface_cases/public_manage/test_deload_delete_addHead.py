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


class TestCase():
        value = 1
        @allure.step("接口test_addHead")
        def test_addHead(self):
            payload1 = {
                        'accessToken':config.TOKEN,
                        "content": {
                            'fileName': "金刚-名师@2x.png",
                            'imageUrl': "https://oss.caizidao.com.cn/rpdt/head_image/%E9%87%91%E5%88%9A-%E5%90%8D%E5%B8%88%402x.png"
                            }
            }

            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url+'/cms-api/headLibrary/addHead', data=payload1,headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200,'test_addHead')

        @allure.step("接口test_queryList")
        def test_queryList(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "page": {"pageNum": 1, "pageSize": 20}
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/headLibrary/queryList', data=payload1, headers=headers)
            global value
            value=r1.json()['content']['list'][0]['id']
            return(value)


        @allure.step("接口test_batchDelete")
        def test_batchDelete(self):
            payload1 = {
                'accessToken':config.TOKEN,
                "content": {
                    'idList':[value]
                }
            }

            headers = {
                "Content-Type": "application/json"
            }

            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url+'/cms-api/headLibrary/batchDelete', data=payload1,headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200,'batchDelete')


if __name__ == "__main__":
    pytest.main(['-s', 'test_deload_delete_addHead'])
