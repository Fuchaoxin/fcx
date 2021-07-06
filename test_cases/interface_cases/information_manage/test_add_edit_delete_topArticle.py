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
        value=1
        
        @allure.step("接口test_article_add")
        def test_article_add(self):
            payload1 = {
                        'accessToken':config.TOKEN,
                        "content": {'articleContent': "<p>testtest11111111testtest11111111testtest11111111testtest11111111testtest11111111testtest11111111</p>",
                                    'articleSummary': "testtest11111111",
                                    'articleTitle': "testtest11111111",
                                    'author': "testtest11",
                                    'coverType': 1,
                                    'expressContent': "testtest11111111",
                                    'isPublishNow': 1,
                                    'lstImageDetails': [{'id': 189, 'url': "https://oss.caizidao.com.cn/rpdt/invest_Article/1.jpg"}],
                                    'publishTime': "",
                                    'saleType': 1,
                                    'specialId': 21,
                                    'status': 2,
                                    'summary': "testtest11111111",
                                    'title': "testtest1111111111111111111111111111",
                                    'trialContent': "<p><br></p>",
                                    'trialImageMask': None,
                                    'trialImageUrl': "",
                                    'trialSummary': ""
                            }
            }

            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url+'/ssax-cls-cms-api/article/add', data=payload1,headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200,'test_article_add')

        @allure.step("接口test_articleList")
        def test_articleList(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "page": {"pageNum": 1, "pageSize": 20},
                "content": {"title": "testtest1111111111111111111111111111",
                            "specialId": 21
                            }
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/ssax-cls-cms-api/article/list', data=payload1, headers=headers)
            global value
            value=r1.json()['content']['list'][0]['id']
            print(r1.json()['content']['list'])
            print(value)
            return(value)


        @allure.step("接口test_articleedit")
        def test_articleedit(self):
            payload1 = {
                'accessToken':config.TOKEN,
                "content": {
                                    'articleContent': "<p>testtest11111111testtest11111111testtest11111111testtest11111111testtest11111111testtest11111111</p>",
                                    'articleSummary': "testtest11111111",
                                    'articleTitle': "testtest11111111",
                                    'author': "testtest22",
                                    'coverType': 1,
                                    'expressContent': "testtest11111111",
                                    'isPublishNow': 1,
                                    'lstImageDetails': [{'id': 189, 'name': 1,'url': "https://oss.caizidao.com.cn/rpdt/invest_Article/1.jpg"}],
                                    'id':value,
                                    'publishTime': "2021-06-30 00:00:00",
                                    'saleType': 1,
                                    'specialId': 21,
                                    'status': 2,
                                    'summary': "testtest11111111",
                                    'title': "testtest1111111111111111111111111111",
                                    'trialContent': "<p><br></p>",
                                    'trialImageMask': None,
                                    'trialImageUrl': "",
                                    'trialSummary': "testtest11111111testtest11111111testtest11111111testtest11111111testtest11111111testtest11111111test"
                }
            }

            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url+'/ssax-cls-cms-api/article/edit', data=payload1,headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200,'articleedit')

        @allure.step("接口test_articleDetail")
        def test_articleDetail(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "content": {
                            "id": value
                            }
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/ssax-cls-cms-api/article/detail', data=payload1, headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200, 'articleDetail')

        @allure.step("接口test_articleTop")
        def test_articleTop(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "content": {
                        "id": value
                 }
             }
            headers = {
                    "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/ssax-cls-cms-api/article/top', data=payload1,
                                   headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200, 'articleTop')

        @allure.step("接口test_articleDelete")
        def test_articleDelete(self):
                payload1 = {
                            'accessToken': config.TOKEN,
                            "content": {
                            'id': value
                         }
                }
                headers = {
                            "Content-Type": "application/json"
                            }
                payload1 = json.dumps(payload1)
                r1 = requests.post(url=config.Pre_Url + '/ssax-cls-cms-api/article/delete', data=payload1,
                               headers=headers)
                As = AssertUtil()
                As.assert_code(r1.json()['code'], 200, 'articleDelete')

if __name__ == "__main__":
    pytest.main(['-s', 'test_add_edit_delete_topArticle'])
