#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import allure

@allure.feature('搜索模块')
class TestSearch:
    def test_case1(self):
        print('case1')
        pass

    def test_case2(self):
        print('case2')
        pass

@allure.feature('登录模块')
class TestLogin:
    @allure.story('登录成功')
    def test_login_success(self):
        with allure.step('步骤一：打开应用'):
            print('打开应用')
        with allure.step('步骤二：进入登录页面'):
            print('登录页面')
        with allure.step('输入用户名和密码'):
            print('输入用户名和密码')
        print('这是登录测试用例 登录成功')
        pass

    @allure.story('登录失败')
    def test_login_failure(self):
        print('这是登录测试用例 登录失败')

    @allure.story('用户名缺失')
    def test_login_no_name(self):
        print('用户名缺失')
        pass

    @allure.story('密码缺失')
    def test_login_no_password(self):

        with allure.step('点击用户名'):
            print('输入用户名')
        with allure.step('点击密码'):
            print('输入密码')
        print('点击登录')
        with allure.step('点击登录之后登录失败'):
            assert '1' == 1
            print('登录失败')

    @allure.story('登录失败')
    def test_login_failure_b(self):
        print('这是登录测试用例 登录失败')


if __name__=='__main__':
    pytest.main()

