import logging

import app
import utils
from api.apiFactory import ApiFactory
import pytest


@pytest.mark.run(order=0)
class TestUserApi:

    def test_get_token(self):
        res = ApiFactory.get_user_api().get_token_api()
        # 打印请求地址 打印请求参数 打印请求响应数据
        logging.info("请求地址:{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        utils.common_assert_code(res)
        assert len(res.json().get("token")) > 0
        app.headers["token"] = res.json().get("token")
        print("app.headers:{}".format(app.headers))

    def test_token_verify_api(self):
        res = ApiFactory.get_user_api().token_verify_api()
        # 打印请求地址 打印请求参数 打印请求响应数据
        logging.info("请求地址:{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        utils.common_assert_code(res)
        assert res.json().get("isValid") is True

    def test_user_address(self):
        """用户地址信息"""
        # 响应对象
        res = ApiFactory.get_user_api().user_address_api()
        # 打印请求地址 打印请求参数 打印请求响应数据
        logging.info("请求地址:{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        utils.common_assert_code(res)
        assert False not in [i in res.text for i in ["诸葛村夫", "18800000001", "北京市", "昌平区"]]
