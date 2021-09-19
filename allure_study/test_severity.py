#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
project: allureProject
file: test_severity
author: bytedance
creat date: 2021/9/19 6:03 下午

'''
import allure
import pytest


def test_with_no_severity_label():
    pass

@allure.severity(allure.severity_level.TRIVIAL)
def test_with_trivial_severity():
    pass

@allure.severity(allure.severity_level.NORMAL)
def test_with_nomal_severity():
    pass

@allure.severity(allure.severity_level.NORMAL)
class TestClassWithNomalSeverity:
    def test_inside_the_nomal_severity_test_class(self):
        pass
    @allure.severity(allure.severity_level.CRITICAL)
    def test_inside_the_nomal_severity_test_class_with_overriding_critical_severity(self):
        pass

if __name__=="__main__":
    pytest.main




