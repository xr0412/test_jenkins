import allure


class TestAttach:

    @allure.step('登录操作')
    def test_001(self):
        # 用户名
        allure.attach('登录用户名', '13611110000')
        # 密码
        allure.attach('登录密码', '123456')
        assert True
