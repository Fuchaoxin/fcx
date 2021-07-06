# -*- coding: utf-8 -*-
import requests
import pytest
import allure
from base import config
import json
from base.AssertUtil import AssertUtil
class TestCase:
        value=1

        @allure.step("接口test_imageadd")
        def test_imageadd(self):
            payload1 = {
                'accessToken':config.TOKEN,
                "content": {'lstImageListModel': [{'name': "43X34", 'url': "https://oss.caizidao.com.cn/rpdt/specialColumn_manage/43X34.png"}]}
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url+'/ssax-cls-cms-api/image/add', data=payload1,headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200,'test_imageadd')

        @allure.step("接口test_imageList")
        def test_imageList(self):
            payload1 = {
                'accessToken':config.TOKEN,
                "page":{"pageNum": 1,"pageSize":20},
                "content": {"name": ""}
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url+'/ssax-cls-cms-api/image/list', data=payload1,headers=headers)
            global value
            value = r1.json()['content']['list'][0]['id']
            return value

        @allure.step("接口test_imagedelete")
        def test_imagedelete(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "content": {
                    'idList': [value]
                }
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/ssax-cls-cms-api/image/delete', data=payload1, headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200, 'test_imagedelete')


if __name__ == "__main__":

    pytest.main(['-s','test_add_deleteimage.py'])
