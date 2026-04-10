# -*- coding: utf-8 -*-
# @Author : ben
# @Time : 2024/7/23 10:32

import allure

from core.assert_util import assert_equal
from service.register_service import (
    Jp_email_maxtime,
    Jp_email_repeat,
    Jp_get_email_code,
    Jp_register_code_fail,
    email_pwd_reset_get_code,
    email_pwd_reset_isregister,
    email_pwd_reset_repeat_code,
    email_repeat_code,
    pwd_reset_get_code,
    pwd_reset_phone_isregister,
    pwd_reset_repeat_code,
    register_code_fail,
    register_code_null,
    register_phone_repeat,
    repeat_code,
)


@allure.feature("注册登录")
@allure.title("验证错误的密码登陆")
def test_check_login_passage_error(register_login_data, login_service, log):
    log.info("--------------start-------------")
    with allure.step("调用 service：登录校验"):
        r2 = login_service.check_login_passage_error()
    log.info("先输入手机号码")
    log.info("再输入错误密码")
    with allure.step("assert_util 断言"):
        assert_equal(str(r2), "20006", "错误密码测试用例不通过")
    log.info("--------------end-------------")


@allure.feature("注册登录")
@allure.title("验证空密码登陆")
def test_check_login_passage_null(register_login_data, login_service, log):
    log.info("--------------start-------------")
    with allure.step("调用 service：登录校验"):
        r2 = login_service.check_login_passage_null()
    log.info("先输入手机号码")
    log.info("再输入空密码")
    with allure.step("assert_util 断言"):
        assert_equal(str(r2), "10010", "空密码测试用例不通过")
    log.info("--------------end-------------")


@allure.feature("注册登录")
@allure.title("验证未注册手机号码登陆")
def test_check_login_passage_exist(register_login_data, login_service, log):
    log.info("--------------start-------------")
    with allure.step("调用 service：登录校验"):
        r2 = login_service.check_login_passage_exist()
    log.info("先输入未注册手机号码")
    log.info("再输入正确密码")
    with allure.step("assert_util 断言"):
        assert_equal(str(r2), "40008", "未注册手机号码测试用例不通过")
    log.info("--------------end-------------")


@allure.feature("注册登录")
@allure.title("错误验证码注册手机账号")
def test_register_code_fail(register_login_data, log):
    log.info("--------------start-------------")
    with allure.step("调用 service：注册流程"):
        r2 = register_code_fail()
    log.info("先输入正确的手机号码")
    log.info("输入错误的验证码")
    log.info("点击注册按钮")
    with allure.step("assert_util 断言"):
        assert_equal(str(r2), "40024", "错误验证码注册账号测试用例不通过")
    log.info("--------------end-------------")


@allure.feature("注册登录")
@allure.title("验证码为空注册")
def test_register_code_null(register_login_data, log):
    log.info("--------------start-------------")
    with allure.step("调用 service：注册流程"):
        r2 = register_code_null()
    log.info("先输入未注册手机号码")
    log.info("不输入验证码")
    log.info("点击注册按钮")
    with allure.step("assert_util 断言"):
        assert_equal(str(r2), "10010", "未注册手机号码测试用例不通过")
    log.info("--------------end-------------")


@allure.feature("注册登录")
@allure.title("验证重复手机号码进行注册")
def test_register_phone_repeat(register_login_data, log):
    log.info("--------------start-------------")
    with allure.step("调用 service：注册流程"):
        r2 = register_phone_repeat()
    log.info("先输入已注册手机号码")
    log.info("点击获取验证码按钮")
    with allure.step("assert_util 断言"):
        assert_equal(str(r2), "40030", "重复手机号码进行注册测试用例不通过")
    log.info("--------------end-------------")


@allure.feature("注册登录")
@allure.title("验证手机号码格式")
def test_register_phone_format(register_login_data, log):
    log.info("--------------start-------------")
    with allure.step("调用 service：注册流程"):
        r2 = register_phone_repeat()
    log.info("先输入不符合规则手机号码")
    log.info("点击获取验证码按钮")
    with allure.step("assert_util 断言"):
        assert_equal(str(r2), "40030", "手机号码格式测试用例不通过")
    log.info("--------------end-------------")


@allure.feature("注册登录")
@allure.title("重复获取手机验证码")
def test_repeat_code(register_login_data, log):
    log.info("--------------start-------------")
    with allure.step("调用 service：重复获取验证码"):
        repeat_code()
        r2 = repeat_code()
    log.info("先输入符合规则手机号码")
    log.info("点击获取验证码按钮")
    log.info("再次获取验证码按钮")
    with allure.step("assert_util 断言"):
        assert_equal(str(r2), "40032", "重复获取手机验证码测试用例不通过")
    log.info("--------------end-------------")


@allure.feature("注册登录")
@allure.title("日本服务器邮箱登陆")
def test_check_login_passage_success(register_login_data, login_service, log):
    log.info("--------------start-------------")
    with allure.step("调用 service：登录"):
        r2 = login_service.check_login_passage_success()
    log.info("先输入符合规则邮箱")
    log.info("输入正确的密码")
    log.info("点击登陆按钮")
    with allure.step("assert_util 断言"):
        assert_equal(str(r2), "0", "日本邮箱登陆测试用例不通过")
    log.info("--------------end-------------")


@allure.feature("注册登录")
@allure.title("切换日本服务器")
def test_exchange_country_list(register_login_data, login_service, log):
    log.info("--------------start-------------")
    with allure.step("调用 service：国家列表"):
        r2 = login_service.exchange_country_list()
    log.info("进入国家列表/地区界面")
    log.info("输入日本")
    log.info("点击搜索按钮")
    with allure.step("assert_util 断言"):
        assert_equal(r2, "日本", "切换日本节点测试用例不通过")
    log.info("--------------end-------------")


@allure.feature("注册登录")
@allure.title("错误验证码注册邮箱账号")
def test_Jp_register_code_fail(register_login_data, log):
    log.info("--------------start-------------")
    with allure.step("调用 service：日区注册"):
        r2 = Jp_register_code_fail()
    log.info("先输入未注册的邮箱")
    log.info("输入错误的验证码")
    log.info("输入两次一致的密码")
    log.info("点击完成注册按钮")
    with allure.step("assert_util 断言"):
        assert_equal(str(r2), "40024", "错误验证码注册账号测试用例不通过")
    log.info("--------------end-------------")


@allure.feature("注册登录")
@allure.title("验证正常获取邮箱验证码")
def test_Jp_get_email_code(register_login_data, log):
    log.info("--------------start-------------")
    with allure.step("调用 service：获取邮箱验证码"):
        r2 = Jp_get_email_code()
    log.info("先输入未注册的邮箱")
    log.info("点击获取验证码按钮")
    with allure.step("assert_util 断言"):
        assert_equal(r2, "Success！", "测试用例不通过")
    log.info("--------------end-------------")


@allure.feature("注册登录")
@allure.title("验证已注册邮箱重新去注册")
def test_Jp_email_repeat(register_login_data, log):
    log.info("--------------start-------------")
    with allure.step("调用 service：邮箱注册校验"):
        r2 = Jp_email_repeat()
    log.info("先输入已注册的邮箱")
    log.info("点击获取验证码按钮")
    with allure.step("assert_util 断言"):
        assert_equal(str(r2), "40030", "测试用例不通过")
    log.info("--------------end-------------")


@allure.feature("注册登录")
@allure.title("验证请求验证码已达上限")
def test_Jp_email_maxtime(register_login_data, log):
    log.info("--------------start-------------")
    with allure.step("调用 service：验证码上限"):
        r2 = Jp_email_maxtime()
    log.info("先输入未注册的邮箱")
    log.info("第5次点击获取验证码按钮")
    with allure.step("assert_util 断言"):
        assert_equal(str(r2), "40045", "测试用例不通过")
    log.info("--------------end-------------")


@allure.feature("注册登录")
@allure.title("重复获取邮箱验证码")
def test_email_repeat_code(register_login_data, log):
    log.info("--------------start-------------")
    with allure.step("调用 service：重复获取邮箱验证码"):
        email_repeat_code()
        r2 = email_repeat_code()
    log.info("先输入符合规则邮箱")
    log.info("点击获取验证码按钮")
    log.info("再次获取验证码按钮")
    with allure.step("assert_util 断言"):
        assert_equal(str(r2), "40032", "重复获取邮箱验证码测试用例不通过")
    log.info("--------------end-------------")


@allure.feature("注册登录")
@allure.title("未注册的邮箱重置密码")
def test_email_pwd_reset_isregister(register_login_data, log):
    log.info("--------------start-------------")
    with allure.step("调用 service：重置密码校验"):
        r2 = email_pwd_reset_isregister()
    log.info("先进入重置密码界面")
    log.info("输入未注册的邮箱")
    log.info("点击获取验证码按钮")
    with allure.step("assert_util 断言"):
        assert_equal(str(r2), "40008", "测试用例不通过")
    log.info("--------------end-------------")


@allure.feature("注册登录")
@allure.title("重置密码-正常获取邮箱验证码")
def test_email_pwd_reset_get_code(register_login_data, log):
    log.info("--------------start-------------")
    with allure.step("调用 service：重置密码获取验证码"):
        r2 = email_pwd_reset_get_code()
    log.info("先输入已注册的邮箱")
    log.info("点击获取验证码按钮")
    with allure.step("assert_util 断言"):
        assert_equal(r2, "Success！", "邮箱未注册测试用例不通过")
    log.info("--------------end-------------")


@allure.feature("注册登录")
@allure.title("重置密码界面重复获取邮箱验证码")
def test_email_pwd_reset_repeat_code(register_login_data, log):
    log.info("--------------start-------------")
    with allure.step("调用 service：重复获取邮箱验证码"):
        email_pwd_reset_repeat_code()
        r2 = email_pwd_reset_repeat_code()
    log.info("先输入未注册的邮箱")
    log.info("点击获取验证码按钮")
    log.info("再次点击获取验证码按钮")
    with allure.step("assert_util 断言"):
        assert_equal(str(r2), "40032", "邮箱可以重复获取验证码测试用例不通过")
    log.info("--------------end-------------")


@allure.feature("注册登录")
@allure.title("未注册的手机号码重置密码")
def test_pwd_reset_phone_isregister(register_login_data, log):
    log.info("--------------start-------------")
    with allure.step("调用 service：重置密码校验"):
        r2 = pwd_reset_phone_isregister()
    log.info("先进入重置密码界面")
    log.info("输入未注册的邮箱")
    log.info("点击获取验证码按钮")
    with allure.step("assert_util 断言"):
        assert_equal(str(r2), "40008", "测试用例不通过")
    log.info("--------------end-------------")


@allure.feature("注册登录")
@allure.title("重置密码界面正常获取手机验证码")
def test_pwd_reset_get_code(register_login_data, log):
    log.info("--------------start-------------")
    with allure.step("调用 service：重置密码获取手机验证码"):
        r2 = pwd_reset_get_code()
    log.info("先输入已注册的手机号码")
    log.info("点击获取验证码按钮")
    with allure.step("assert_util 断言"):
        assert_equal(r2, "Success！", "手机号码未注册测试用例不通过")
    log.info("--------------end-------------")


@allure.feature("注册登录")
@allure.title("重置密码界面重复获取手机验证码")
def test_pwd_reset_repeat_code(register_login_data, log):
    log.info("--------------start-------------")
    with allure.step("调用 service：重复获取手机验证码"):
        pwd_reset_repeat_code()
        r2 = pwd_reset_repeat_code()
    log.info("先输入已注册的手机号码")
    log.info("点击获取验证码按钮")
    log.info("再次点击获取验证码按钮")
    with allure.step("assert_util 断言"):
        assert_equal(str(r2), "40032", "邮箱可以重复获取验证码测试用例不通过")
    log.info("--------------end-------------")
