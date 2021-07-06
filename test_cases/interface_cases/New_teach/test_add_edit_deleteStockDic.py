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

class TestCase():
        value=1
        value1=1
        
        @allure.step("接口test_addStockDicClassify")
        def test_addStockDicClassify(self):
            payload1 = {
                'accessToken':config.TOKEN,
                "content": {
                                'id': None,
                                'name': "test111111",
                                'uploadImageUrl': "https://oss.caizidao.com.cn/rpdt/invest_educat/dictory72.png"
                            }
            }

            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url+'/cms-api/stockDicManage/addStockDicClassify', data=payload1,headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 1,'addStockDicClassify')

        @allure.step("接口test_getStockDicClassifyList")
        def test_getStockDicClassifyList(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "page": {"pageNum": 1, "pageSize": 20},
                "content": {
                    "keyword": ""
                }
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/stockDicManage/getStockDicClassifyList', data=payload1,
                               headers=headers)
            global value
            value = r1.json()['content']['list'][0]['id']
            print(value)
            return (value)

        @allure.step("接口test_editStockDicClassify")
        def test_editStockDicClassify(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "content": {
                                'createTime': 1625190726000,
                                'creater': "bailingyu",
                                'id': value,
                                'isDeleted': 'false',
                                'modifyTime': 1625190726000,
                                'name': "test1111112222",
                                'sortNum': '-25',
                                'uploadImageUrl': "https://oss.caizidao.com.cn/rpdt/invest_educat/dictory72.png"
                }
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/stockDicManage/editStockDicClassify', data=payload1,
                               headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200, 'editStockDicClassify')

        @allure.step("接口test_stockDicClassifyMoveUpOrDown")
        def test_stockDicClassifyMoveUpOrDown(self):
            payload1 = {
                'accessToken': config.TOKEN,
                'page': {'pageNum': 1, 'pageSize': 20},
                "content": {
                            'classifyId': value,
                            'keyword': "",
                            'step': '1'
                }
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/stockDicManage/stockDicClassifyMoveUpOrDown', data=payload1,
                               headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200, 'stockDicClassifyMoveUpOrDown')

        @allure.step("接口test_getUploadVideoAddressAuth")
        def test_getUploadVideoAddressAuth(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "content": {
                    'fileName': "1.mp4"
                }
            }
            headers = {
                "Content-Type": "application/json"
            }
            print(value)
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/vodUploadAuth/getUploadVideoAddressAuth', data=payload1,
                               headers=headers)
            global value2
            value2 = r1.json()['content']['videoId']
            return (value2)

        @allure.step("接口test_addStockDic")
        def test_addStockDic(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "content": {
                                'classifyId': value,
                                'dicCoverImg': "blob:https://rpdtssax-cms.caizidao.com.cn:9011/555055d4-05bd-4af1-80ab-b6073432fb00",
                                'dicExplain': "时擦出飒飒吃撒吃撒吃啥菜",
                                'dicVideo': value2,
                                'duration': 1.112,
                                'id': None,
                                'isVideo': 'true',
                                'isWord': 'true',
                                'keyword': "11111",
                                'name': "test1111111"
                }
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/stockDicManage/addStockDic', data=payload1,
                               headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 1, 'addStockDic')

        @allure.step("接口test_getStockDicList")
        def test_getStockDicList(self):
            payload1 = {
                'accessToken': config.TOKEN,
                'page': {'pageNum': 1, 'pageSize': 20},
                "content": {
                    'classifyId': value,
                    'keyword': ""
                }
            }
            headers = {
                "Content-Type": "application/json"
            }
            print(value)
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/stockDicManage/getStockDicList', data=payload1,
                               headers=headers)
            global value1
            value1 = r1.json()['content']['list'][0]['id']
            return (value1)

        @allure.step("接口test_editStockDic")
        def test_editStockDic(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "content": {
                            'classifyId': value,
                            'classifyName': "test1111112222",
                            'createTime': 1625191375000,
                            'creater': "bailingyu",
                            'delFlag': None,
                            'dicCoverImg': "blob:https://rpdtssax-cms.caizidao.com.cn:9011/555055d4-05bd-4af1-80ab-b6073432fb00",
                            'dicExplain': "时擦出飒飒吃撒吃撒吃啥菜",
                            'dicVideo': "a84fe0d7d7344309948df65622b5d8cd",
                            'duration': 1.112,
                            'id': value1,
                            'isDeleted': 'false',
                            'isVideo': 'true',
                            'isWord': 'true',
                            'keyword': "11111",
                            'modifyTime': 1625191375000,
                            'name': "test11113333",
                            'sortNum': '-2',
                            'stockDicIdList': None,
                            'stockDicVideoSetIdList': None,
                            'videoSetName': None
                }
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/stockDicManage/editStockDic', data=payload1,
                               headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200, 'editStockDic')

        @allure.step("接口test_batchEditStockDic")
        def test_batchEditStockDic(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "content": {
                            'delFlag': 'true',
                            'isDeleted': 'true',
                            'stockDicIdList': [value1]
                }
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/stockDicManage/batchEditStockDic', data=payload1,
                               headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200, 'batchEditStockDic')

        @allure.step("接口test_batchEditStockDicClassify")
        def test_batchEditStockDicClassify(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "content": {
                    'delFlag': 'true',
                    'isDeleted': 'true',
                    'stockDicClassifyIdList': [value]
                }
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/stockDicManage/batchEditStockDicClassify', data=payload1,
                               headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200, 'batchEditStockDicClassify')

if __name__ == "__main__":
    pytest.main(['-s', 'test_add_edit_deleteStockDic'])
