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
                                    'isPublishNow': 0,
                                    'lstImageDetails': [{'id': 189, 'url': "https://oss.caizidao.com.cn/rpdt/invest_Article/1.jpg"}],
                                    'publishTime': "2021-06-30 00:00:00",
                                    'saleType': 2,
                                    'specialId': 28,
                                    'status': 1,
                                    'summary': "testtest11111111",
                                    'title': "testtest1111111111111111111111111111",
                                    'trialContent': "<p>testtest11111111testtest11111111testtest11111111testtest11111111testtest11111111testtest11111111testtest11111111testtest11111111testtest11111111testtest11111111testtest11111111testtest11111111</p>",
                                    'trialImageMask': 69,
                                    'trialImageUrl': "https://oss.caizidao.com.cn/rpdt/invest_Article/690X320X1.png",
                                    'trialSummary': "testtest11111111testtest11111111testtest11111111testtest11111111testtest11111111testtest11111111test"
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
                "page": {"pageNum": 1, "pageSize": 500},
                "content": {"title": "testtest1111111111111111111111111111",
                            "status": 1
                            }
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/ssax-cls-cms-api/article/list', data=payload1, headers=headers)
            print(r1.json()['content']['list'][0]['id'])
            return(r1.json()['content']['list'][0]['id'])


        @allure.step("接口test_articleedit")
        def test_articleedit(self):
            payload1 = {
                'accessToken':config.TOKEN,
                "content": {
                                    'articleContent': "<p>testtest11111111testtest11111111testtest11111111testtest11111111testtest11111111testtest11111111</p>",
                                    'articleSummary': "testtest11111111",
                                    'articleTitle': "testtest11111111",
                                    'author': "testtest11",
                                    'coverType': 1,
                                    'expressContent': "testtest11111111",
                                    'isPublishNow': 0,
                                    'lstImageDetails': [{'id': 189, 'name': 1,'url': "https://oss.caizidao.com.cn/rpdt/invest_Article/1.jpg"}],
                                    'id':self.test_articleList(),
                                    'publishTime': "2021-06-30 00:00:00",
                                    'saleType': 2,
                                    'specialId': 28,
                                    'status': 1,
                                    'summary': "testtest11111111",
                                    'title': "testtest1111111111111111111111111111",
                                    'trialContent': "<p>testtest11111111testtest11111111testtest11111111testtest11111111testtest11111111testtest11111111testtest11111111testtest11111111testtest11111111testtest11111111testtest11111111testtest11111111</p>",
                                    'trialImageMask': 69,
                                    'trialImageUrl': "https://oss.caizidao.com.cn/rpdt/invest_Article/690X320X1.png",
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


        @allure.step("接口test_articleDelete")
        def test_articleDelete(self):
                payload1 = {
                            'accessToken': config.TOKEN,
                            "content": {
                            'id': self.test_articleList()
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
    pytest.main(['-s', 'test_add_close_deleteArticle'])
