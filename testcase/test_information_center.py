# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/08/1
# @Author : huanggenghao

import allure

from core.assert_util import assert_equal


@allure.feature("消息中心")
@allure.title("系统通知点击全部已读")
def test_system_all_read(message_center_data, message_service, log):
    log.info("--------------start-------------")
    with allure.step("调用 service：消息中心全部已读"):
        r2 = message_service.information_center(1, "zh_CN")
    log.info("登陆手机账号15992213991")
    log.info("切换到首页")
    log.info("进入消息中心")
    log.info("系统通知点击全部已读按钮")
    with allure.step("assert_util 断言"):
        assert_equal(r2, "Success！", "测试用例不通过")
    log.info("--------------end-------------")


@allure.feature("消息中心")
@allure.title("设备推送点击全部已读")
def test_device(message_center_data, message_service, log):
    log.info("--------------start-------------")
    with allure.step("调用 service：消息中心全部已读"):
        r2 = message_service.information_center(3, "zh_CN")
    log.info("登陆手机账号15992213991")
    log.info("切换到首页")
    log.info("进入消息中心")
    log.info("设备推送点击全部已读")
    with allure.step("assert_util 断言"):
        assert_equal(r2, "Success！", "测试用例不通过")
    log.info("--------------end-------------")


@allure.feature("消息中心")
@allure.title("设备分享点击全部已读")
def test_device_sharing(message_center_data, message_service, log):
    log.info("--------------start-------------")
    with allure.step("调用 service：消息中心全部已读"):
        r2 = message_service.information_center(4, "zh_CN")
    log.info("登陆手机账号15992213991")
    log.info("切换到首页")
    log.info("进入消息中心")
    log.info("设备分享点击全部已读")
    with allure.step("assert_util 断言"):
        assert_equal(r2, "Success！", "测试用例不通过")
    log.info("--------------end-------------")


@allure.feature("消息中心")
@allure.title("系统通知点击全部已读(英文)")
def test_system_all_read_english(message_center_data, message_service, log):
    log.info("--------------start-------------")
    with allure.step("调用 service：消息中心全部已读"):
        r2 = message_service.information_center(1, "en_US")
    log.info("登陆手机账号15992213991")
    log.info("切换到首页")
    log.info("进入消息中心")
    log.info("系统通知点击全部已读按钮")
    with allure.step("assert_util 断言"):
        assert_equal(r2, "Success！", "测试用例不通过")
    log.info("--------------end-------------")


@allure.feature("消息中心")
@allure.title("设备推送点击全部已读(英文)")
def test_device_english(message_center_data, message_service, log):
    log.info("--------------start-------------")
    with allure.step("调用 service：消息中心全部已读"):
        r2 = message_service.information_center(3, "en_US")
    log.info("登陆手机账号15992213991")
    log.info("切换到首页")
    log.info("进入消息中心")
    log.info("设备推送点击全部已读")
    with allure.step("assert_util 断言"):
        assert_equal(r2, "Success！", "测试用例不通过")
    log.info("--------------end-------------")


@allure.feature("消息中心")
@allure.title("设备分享点击全部已读(英文)")
def test_device_sharing_english(message_center_data, message_service, log):
    log.info("--------------start-------------")
    with allure.step("调用 service：消息中心全部已读"):
        r2 = message_service.information_center(4, "en_US")
    log.info("登陆手机账号15992213991")
    log.info("切换到首页")
    log.info("进入消息中心")
    log.info("设备分享点击全部已读")
    with allure.step("assert_util 断言"):
        assert_equal(r2, "Success！", "测试用例不通过")
    log.info("--------------end-------------")
