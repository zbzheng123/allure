#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
project: allureProject
file: test_case
author: bytedance
creat date: 2021/9/19 5:34 下午

'''

import allure

TEST_CASE_LINK = 'https://www.baidu.com/'

@allure.testcase(TEST_CASE_LINK, '测试链接')
def test_with_testcase_link():
    pass