# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/07/26
# @Author : huanggenghao

import allure

from core.assert_util import assert_equal


@allure.feature("个人中心")
@allure.title("验证更新用户名称")
def test_update_user_data(user_mine_data, user_service, log):
    log.info("--------------start-------------")
    with allure.step("调用 service：更新用户昵称"):
        r2 = user_service.update_user_data()
    log.info("登陆手机账号15992213991")
    log.info("切换到个人中心")
    log.info("修改昵称信息为13570368266")
    log.info("点击确定按钮")
    with allure.step("assert_util 断言"):
        assert_equal(r2, "Success", "测试用例不通过")
    log.info("--------------end-------------")


@allure.feature("个人中心")
@allure.title("验证更新用户名称为空")
def test_update_user_data_null(user_mine_data, user_service, log):
    log.info("--------------start-------------")
    with allure.step("调用 service：昵称为空"):
        r2 = user_service.update_user_data_null()
    log.info("登陆手机账号15992213991")
    log.info("切换到个人中心")
    log.info("修改昵称信息为空")
    log.info("点击确定按钮")
    with allure.step("assert_util 断言"):
        assert_equal(r2, "Success", "测试用例不通过")
    log.info("--------------end-------------")


@allure.feature("个人中心")
@allure.title("验证更新用户名称为1")
def test_update_user_data_one(user_mine_data, user_service, log):
    log.info("--------------start-------------")
    with allure.step("调用 service：昵称为1"):
        r2 = user_service.update_user_data_one()
    log.info("登陆手机账号15992213991")
    log.info("切换到个人中心")
    log.info("修改昵称信息为1")
    log.info("点击确定按钮")
    with allure.step("assert_util 断言"):
        assert_equal(r2, "Success", "测试用例不通过")
    log.info("--------------end-------------")


@allure.feature("个人中心")
@allure.title("验证更新用户名称超长")
def test_update_user_data_enought(user_mine_data, user_service, log):
    log.info("--------------start-------------")
    with allure.step("调用 service：昵称超长"):
        r2 = user_service.update_user_data_enought()
    log.info("登陆手机账号15992213991")
    log.info("切换到个人中心")
    log.info("修改昵称信息为1111111111111111111111111111111111")
    log.info("点击确定按钮")
    with allure.step("assert_util 断言"):
        assert_equal(r2, "Success", "测试用例不通过")
    log.info("--------------end-------------")


@allure.feature("个人中心")
@allure.title("验证修改用户头像")
def test_update_user_avatar_success(user_mine_data, user_service, log):
    log.info("--------------start-------------")
    with allure.step("调用 service：更新头像"):
        r2 = user_service.update_user_avatar_success()
    log.info("登陆手机账号15992213991")
    log.info("切换到个人中心")
    log.info("修改用户头像")
    log.info("点击确定按钮")
    with allure.step("assert_util 断言"):
        assert_equal(r2, "Success", "测试用例不通过")
    log.info("--------------end-------------")


@allure.feature("个人中心")
@allure.title("验证修改用户头像为默认头像")
def test_update_user_avatar_null(user_mine_data, user_service, log):
    log.info("--------------start-------------")
    with allure.step("调用 service：头像为空"):
        r2 = user_service.update_user_avatar_null()
    log.info("登陆手机账号15992213991")
    log.info("切换到个人中心")
    log.info("修改用户头像为空")
    log.info("点击确定按钮")
    with allure.step("assert_util 断言"):
        assert_equal(r2, "Success", "测试用例不通过")
    log.info("--------------end-------------")


@allure.feature("个人中心")
@allure.title("验证修改用户昵称为30个字符")
def test_update_user_avatar_third(user_mine_data, user_service, log):
    log.info("--------------start-------------")
    with allure.step("调用 service：昵称30字符"):
        r2 = user_service.update_user_avatar_third()
    log.info("登陆手机账号15992213991")
    log.info("切换到个人中心")
    log.info("修改用户昵称刚好30个字符")
    log.info("点击确定按钮")
    with allure.step("assert_util 断言"):
        assert_equal(r2, "Success", "测试用例不通过")
    log.info("--------------end-------------")


@allure.feature("个人中心")
@allure.title("验证获取推送开关列表默认状态")
def test_push_switch_list(user_mine_data, user_service, log):
    log.info("--------------start-------------")
    with allure.step("调用 service 接口"):
        r2 = user_service.push_switch_list()
    log.info("登陆手机账号15992213991")
    log.info("切换我的")
    log.info("进入消息设置界面")
    log.info("查看消息设置默认值")
    with allure.step("assert_util 断言"):
        assert_equal(r2, "Success！", "测试用例不通过")
    log.info("--------------end-------------")


@allure.feature("个人中心")
@allure.title("设备推送开关为开")
def test_push_switch_update(user_mine_data, user_service, log):
    log.info("--------------start-------------")
    with allure.step("调用 service 接口"):
        r2 = user_service.push_switch_update()
    log.info("登陆手机账号15992213991")
    log.info("切换我的")
    log.info("进入消息设置界面")
    log.info("设置推送开关为开")
    with allure.step("assert_util 断言"):
        assert_equal(r2, "Success！", "测试用例不通过")
    log.info("--------------end-------------")


@allure.feature("个人中心")
@allure.title("设置设备分享为关")
def test_push_switch_update_01(user_mine_data, user_service, log):
    log.info("--------------start-------------")
    with allure.step("调用 service 接口"):
        r2 = user_service.push_switch_update_01()
    log.info("登陆手机账号15992213991")
    log.info("切换我的")
    log.info("进入消息设置界面")
    log.info("设置设备分享为关")
    with allure.step("assert_util 断言"):
        assert_equal(r2, "Success！", "测试用例不通过")
    log.info("--------------end-------------")


@allure.feature("个人中心")
@allure.title("设置系统通知为关")
def test_push_switch_update_02(user_mine_data, user_service, log):
    log.info("--------------start-------------")
    with allure.step("调用 service 接口"):
        r2 = user_service.push_switch_update_02()
    log.info("登陆手机账号15992213991")
    log.info("切换我的")
    log.info("进入消息设置界面")
    log.info("设置系统通知为关")
    with allure.step("assert_util 断言"):
        assert_equal(r2, "Success！", "测试用例不通过")
    log.info("--------------end-------------")


@allure.feature("个人中心")
@allure.title("检查安卓处于中文下检测到版本更新")
def test_check_version_update_android_china(user_mine_data, user_service, log):
    log.info("--------------start-------------")
    with allure.step("调用 service 接口"):
        r2 = user_service.check_version_update_android_china()
    log.info("登陆手机账号15992213991")
    log.info("切换我的")
    log.info("进入关于界面")
    log.info("点击APP版本")
    with allure.step("assert_util 断言"):
        assert_equal(r2, "Success！", "测试用例不通过")
    log.info("--------------end-------------")


@allure.feature("个人中心")
@allure.title("检查安卓处于中文下相同versioncode检测不到新版本")
def test_check_version_update_android_china_invail(user_mine_data, user_service, log):
    log.info("--------------start-------------")
    with allure.step("调用 service 接口"):
        r2 = user_service.check_version_update_android_china_invail()
    log.info("登陆手机账号15992213991")
    log.info("切换我的")
    log.info("进入关于界面")
    log.info("点击APP版本")
    with allure.step("assert_util 断言"):
        assert_equal(r2, "当前版本已经是最新！", "测试用例不通过")
    log.info("--------------end-------------")


@allure.feature("个人中心")
@allure.title("检查安卓处于中文下应用版本比较异常")
def test_check_version_update_android_china_error(user_mine_data, user_service, log):
    log.info("--------------start-------------")
    with allure.step("调用 service 接口"):
        r2 = user_service.check_version_update_android_china_error()
    log.info("登陆手机账号15992213991")
    log.info("切换我的")
    log.info("进入关于界面")
    log.info("点击APP版本")
    with allure.step("assert_util 断言"):
        assert_equal(r2, "应用版本比较异常！", "测试用例不通过")
    log.info("--------------end-------------")


@allure.feature("个人中心")
@allure.title("检查安卓处于英文下检测到版本更新")
def test_check_version_update_android_english(user_mine_data, user_service, log):
    log.info("--------------start-------------")
    with allure.step("调用 service 接口"):
        r2 = user_service.check_version_update_android_english()
    log.info("登陆手机账号15992213991")
    log.info("切换我的")
    log.info("切换成英语")
    log.info("进入关于界面")
    log.info("点击APP版本")
    with allure.step("assert_util 断言"):
        assert_equal(r2, "Success！", "测试用例不通过")
    log.info("--------------end-------------")


@allure.feature("个人中心")
@allure.title("检查安卓处于英文下相同versioncode检测不到新版本")
def test_check_version_update_android_english_invail(user_mine_data, user_service, log):
    log.info("--------------start-------------")
    with allure.step("调用 service 接口"):
        r2 = user_service.check_version_update_android_english_invail()
    log.info("登陆手机账号15992213991")
    log.info("切换我的")
    log.info("切换成英语")
    log.info("进入关于界面")
    log.info("点击APP版本")
    with allure.step("assert_util 断言"):
        assert_equal(r2, "当前版本已经是最新！", "测试用例不通过")
    log.info("--------------end-------------")


@allure.feature("个人中心")
@allure.title("检查安卓处于英文下应用版本比较异常")
def test_check_version_update_android_english_error(user_mine_data, user_service, log):
    log.info("--------------start-------------")
    with allure.step("调用 service 接口"):
        r2 = user_service.check_version_update_android_english_error()
    log.info("登陆手机账号15992213991")
    log.info("切换我的")
    log.info("切换成英语")
    log.info("进入关于界面")
    log.info("点击APP版本")
    with allure.step("assert_util 断言"):
        assert_equal(r2, "应用版本比较异常！", "测试用例不通过")
    log.info("--------------end-------------")


@allure.feature("个人中心")
@allure.title("检查苹果处于中文下检测到版本更新")
def test_check_version_update_ios_china(user_mine_data, user_service, log):
    log.info("--------------start-------------")
    with allure.step("调用 service 接口"):
        r2 = user_service.check_version_update_ios_china()
    log.info("登陆手机账号15992213991")
    log.info("切换我的")
    log.info("进入关于界面")
    log.info("点击APP版本")
    with allure.step("assert_util 断言"):
        assert_equal(r2, "Success！", "测试用例不通过")
    log.info("--------------end-------------")


@allure.feature("个人中心")
@allure.title("检查苹果处于中文下相同versioncode检测不到新版本")
def test_check_version_update_ios_china_invail(user_mine_data, user_service, log):
    log.info("--------------start-------------")
    with allure.step("调用 service 接口"):
        r2 = user_service.check_version_update_ios_china_invail()
    log.info("登陆手机账号15992213991")
    log.info("切换我的")
    log.info("进入关于界面")
    log.info("点击APP版本")
    with allure.step("assert_util 断言"):
        assert_equal(r2, "当前版本已经是最新！", "测试用例不通过")
    log.info("--------------end-------------")


@allure.feature("个人中心")
@allure.title("检查苹果处于中文下应用版本比较异常")
def test_check_version_update_ios_china_error(user_mine_data, user_service, log):
    log.info("--------------start-------------")
    with allure.step("调用 service 接口"):
        r2 = user_service.check_version_update_ios_china_error()
    log.info("登陆手机账号15992213991")
    log.info("切换我的")
    log.info("进入关于界面")
    log.info("点击APP版本")
    with allure.step("assert_util 断言"):
        assert_equal(r2, "应用版本比较异常！", "测试用例不通过")
    log.info("--------------end-------------")


@allure.feature("个人中心")
@allure.title("检查苹果处于英文下检测到版本更新")
def test_check_version_update_ios_english(user_mine_data, user_service, log):
    log.info("--------------start-------------")
    with allure.step("调用 service 接口"):
        r2 = user_service.check_version_update_ios_english()
    log.info("登陆手机账号15992213991")
    log.info("切换我的")
    log.info("切换成英语")
    log.info("进入关于界面")
    log.info("点击APP版本")
    with allure.step("assert_util 断言"):
        assert_equal(r2, "Success！", "测试用例不通过")
    log.info("--------------end-------------")


@allure.feature("个人中心")
@allure.title("检查苹果处于英文下相同versioncode检测不到新版本")
def test_check_version_update_ios_english_invail(user_mine_data, user_service, log):
    log.info("--------------start-------------")
    with allure.step("调用 service 接口"):
        r2 = user_service.check_version_update_ios_english_invail()
    log.info("登陆手机账号15992213991")
    log.info("切换我的")
    log.info("切换成英语")
    log.info("进入关于界面")
    log.info("点击APP版本")
    with allure.step("assert_util 断言"):
        assert_equal(r2, "当前版本已经是最新！", "测试用例不通过")
    log.info("--------------end-------------")


@allure.feature("个人中心")
@allure.title("检查苹果处于英文下应用版本比较异常")
def test_check_version_update_ios_english_error(user_mine_data, user_service, log):
    log.info("--------------start-------------")
    with allure.step("调用 service 接口"):
        r2 = user_service.check_version_update_ios_english_error()
    log.info("登陆手机账号15992213991")
    log.info("切换我的")
    log.info("切换成英语")
    log.info("进入关于界面")
    log.info("点击APP版本")
    with allure.step("assert_util 断言"):
        assert_equal(r2, "应用版本比较异常！", "测试用例不通过")
    log.info("--------------end-------------")
