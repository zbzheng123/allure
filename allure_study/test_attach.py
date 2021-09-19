#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
project: allureProject
file: test_attach
author: bytedance
creat date: 2021/9/19 7:25 下午

'''

import allure

def test_attach_text():
    allure.attach('这是一个纯文本', attachment_type=allure.attachment_type.TEXT)

def test_attach_html():
    allure.attach('<body>这是一段htmlbody块</body>', 'html测试块', attachment_type=allure.attachment_type.HTML)

def test_attach_photo():
    allure.attach.file('/Users/bytedance/Documents/bug录屏&截图/出版物书籍背景异常.jpg',
                       name='这是一个图片', attachment_type=allure.attachment_type.JPG)

def test_attach_video():
    allure.attach.file('/Users/bytedance/Documents/bug录屏&截图/出版物样式扩展兼容_异常case.mp4',
                       attachment_type=allure.attachment_type.MP4)
