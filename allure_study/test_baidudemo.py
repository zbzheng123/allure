#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
project: allureProject
file: test_baidudemo
author: bytedance
creat date: 2021/9/19 8:03 下午

'''

import allure
import pytest
from selenium import webdriver
from time import sleep

@allure.feature('百度搜索')
@pytest.mark.parametrize('testdata', ['allure', 'pytest', 'unittest'])
def test_steps_demo(testdata):
    with allure.step('打开百度网页'):
        driver = webdriver.Chrome()
        driver.get('https://www.baidu.com/')
        driver.maximize_window()

    with allure.step(f'输入搜索词:{testdata}'):
        driver.find_element_by_id('kw').send_keys(testdata)
        sleep(2)
        driver.find_element_by_id('su').click()
        sleep(2)

    with allure.step('保存图片'):
        driver.save_screenshot('./result/b.png')
        allure.attach.file('./result/b.png', attachment_type=allure.attachment_type.PNG)

    with allure.step('关闭浏览器'):
        driver.quit()



