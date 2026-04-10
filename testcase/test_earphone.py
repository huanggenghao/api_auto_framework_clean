# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/07/31
# @Author : huanggenghao

import allure

from core.assert_util import assert_equal


@allure.feature("耳机说明书")
@allure.title("获取h5耳机说明书")
def test_get_h5_information(earphone_data, earphone_service, log):
    log.info("--------------start-------------")
    with allure.step("调用 service：耳机说明书"):
        r2 = earphone_service.earphone_information_flow(925994607524962304)
    log.info("登陆手机账号15992213991")
    log.info("连接h5耳机")
    log.info("进入更多")
    log.info("查看h5耳机说明书")
    with allure.step("assert_util 断言"):
        assert_equal(r2, "Success！", "测试用例不通过")
    log.info("--------------end-------------")


@allure.feature("耳机说明书")
@allure.title("获取t3 pro耳机说明书")
def test_get_t3_pro_information(earphone_data, earphone_service, log):
    log.info("--------------start-------------")
    with allure.step("调用 service：耳机说明书"):
        r2 = earphone_service.earphone_information_flow(927442686274351104)
    log.info("登陆手机账号15992213991")
    log.info("连接t3 pro耳机")
    log.info("进入更多")
    log.info("查看t3 pro耳机说明书")
    with allure.step("assert_util 断言"):
        assert_equal(r2, "Success！", "测试用例不通过")
    log.info("--------------end-------------")


@allure.feature("耳机说明书")
@allure.title("获取h6 pro耳机说明书")
def test_get_h6_pro_information(earphone_data, earphone_service, log):
    log.info("--------------start-------------")
    with allure.step("调用 service：耳机说明书"):
        r2 = earphone_service.earphone_information_flow(927443095978160128)
    log.info("登陆手机账号15992213991")
    log.info("连接h6 pro耳机")
    log.info("进入更多")
    log.info("查看h6 pro耳机说明书")
    with allure.step("assert_util 断言"):
        assert_equal(r2, "Success！", "测试用例不通过")
    log.info("--------------end-------------")


@allure.feature("耳机说明书")
@allure.title("获取p3耳机说明书")
def test_get_p3_information(earphone_data, earphone_service, log):
    log.info("--------------start-------------")
    with allure.step("调用 service：耳机说明书"):
        r2 = earphone_service.earphone_information_flow(934671368550416384)
    log.info("登陆手机账号15992213991")
    log.info("连接p3耳机")
    log.info("进入更多")
    log.info("查看p3耳机说明书")
    with allure.step("assert_util 断言"):
        assert_equal(r2, "Success！", "测试用例不通过")
    log.info("--------------end-------------")


@allure.feature("耳机说明书")
@allure.title("获取max 5c耳机说明书")
def test_get_max5c_information(earphone_data, earphone_service, log):
    log.info("--------------start-------------")
    with allure.step("调用 service：耳机说明书"):
        r2 = earphone_service.earphone_information_flow(925997015143538688)
    log.info("登陆手机账号15992213991")
    log.info("连接mac 5c耳机")
    log.info("进入更多")
    log.info("查看mac 5c耳机说明书")
    with allure.step("assert_util 断言"):
        assert_equal(r2, "Success！", "测试用例不通过")
    log.info("--------------end-------------")


@allure.feature("耳机说明书")
@allure.title("获取mac5耳机说明书")
def test_get_mac5_information(earphone_data, earphone_service, log):
    log.info("--------------start-------------")
    with allure.step("调用 service：耳机说明书"):
        r2 = earphone_service.earphone_information_flow(925995115073495040)
    log.info("登陆手机账号15992213991")
    log.info("连接mac5耳机")
    log.info("进入更多")
    log.info("查看mac5耳机说明书")
    with allure.step("assert_util 断言"):
        assert_equal(r2, "Success！", "测试用例不通过")
    log.info("--------------end-------------")


@allure.feature("耳机说明书")
@allure.title("获取t6耳机说明书")
def test_get_t6_information(earphone_data, earphone_service, log):
    log.info("--------------start-------------")
    with allure.step("调用 service：耳机说明书"):
        r2 = earphone_service.earphone_information_flow(925994896852246528)
    log.info("登陆手机账号15992213991")
    log.info("连接t6耳机")
    log.info("进入更多")
    log.info("查看t6耳机说明书")
    with allure.step("assert_util 断言"):
        assert_equal(r2, "Success！", "测试用例不通过")
    log.info("--------------end-------------")
