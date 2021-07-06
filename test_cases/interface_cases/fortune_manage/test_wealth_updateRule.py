# -*- coding: utf-8 -*-
import requests
import pytest
import allure
from base import config
import json
from base.AssertUtil import AssertUtil
@allure.step("接口test_wealth_updateRule")
def test_wealth_updateRule():
    payload1 = {
        "accessToken": config.TOKEN,
        'content': {
                'taskList': [
                        {
                        'amount': "3000",
                        'enabled': 'true',
                        'limitAmount': "3",
                        'otherConfig': "{\"duration\":\"1\"}",
                        'otherConfigMap': {'duration': "1"},
                        'status': "0",
                        'taskId': "1001",
                        'taskName': "视频观看3分钟"},
                        {
                        'amount': "3000",
                        'enabled': 'true',
                        'limitAmount': "3",
                        'otherConfig': "{\"wordCount\":\"3\"}",
                        'otherConfigMap': {'wordCount': "3"},
                        'status': "0",
                        'taskId': "1002",
                        'taskName': "视频留言3"},
                        {
                        'amount': "30",
                        'enabled': 'true',
                        'limitAmount': "3",
                        'otherConfig': "{\"minPayment\":\"0.01\"}",
                        'otherConfigMap': {'minPayment': "0.01"},
                        'status': "0",
                        'taskId': "1003",
                        'taskName': "成一笔购买3"},
                        {
                        'amount': "3000",
                        'enabled': 'true',
                        'limitAmount': "3",
                        'otherConfig': None,
                        'otherConfigMap': None,
                        'status': "0",
                        'taskId': "1004",
                        'taskName': "发布原创视频3"},
                        {
                        'amount': "40000",
                        'enabled': 'true',
                        'limitAmount': "3",
                        'otherConfig': None,
                        'otherConfigMap': None,
                        'status': "0",
                        'taskId': "1005",
                        'taskName': "分享3"},
                       {
                        'amount': "3000",
                        'enabled': 'true',
                        'limitAmount': "1",
                        'otherConfig': None,
                        'otherConfigMap': None,
                        'status': "0",
                        'taskId': "1006",
                        'taskName': "完成身份验证3"},
                        {
                        'amount': "3000",
                        'enabled': 'true',
                        'limitAmount': "3",
                        'otherConfig': "{\"wordCount\":\"3\"}",
                        'otherConfigMap': {'wordCount': "3"},
                        'status': "0",
                        'taskId': "1007",
                        'taskName': "记笔记3字"}],
                        'wealthIntroductionList': [
                        {
                        'introduction': "财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富值管理测财富",
                        'name': "什么是财富值aaaaaaamm"},
                        {'name': "d会员权益", 'introduction': "d"},
                        {'name': "3", 'introduction': "3"},
                        {'name': "4", 'introduction': "4"},
                        {'name': "5", 'introduction': "5"},
                        {'name': "6", 'introduction': "6"},
                        {'name': "7", 'introduction': "7"},
                        {'name': "8", 'introduction': "8"},
                        {'name': "9", 'introduction': "9"},
                        {'name': "10", 'introduction': "10"},
                        {'name': "11", 'introduction': "11"},

                        {'name': "12", 'introduction': "12"},

                        {'name': "13", 'introduction': "13"},

                        {'name': "14", 'introduction': "14"},

                        {'name': "15", 'introduction': "15"},

                        {'name': "16", 'introduction': "16"},

                        {'name': "17", 'introduction': "17"},

                        {'name': "18", 'introduction': "18"},

                        {'name': "19", 'introduction': "19"}]

                        }
    }
    headers ={
        "Content-Type":"application/json"
    }
    payload1 = json.dumps(payload1)
    r1 = requests.post(url=config.Pre_Url+'/shopping-cms-api/wealth/updateRule', data=payload1,headers=headers)
    As = AssertUtil()
    As.assert_code(r1.json()['code'], 200,'test_wealth_updateRule')


if __name__ == "__main__":
    test_wealth_updateRule()
    pytest.main(['-s','test_wealth_updateRule.py'])
