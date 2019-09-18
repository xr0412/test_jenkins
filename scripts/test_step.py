import allure


class TestStep:

    @allure.step('登录操作')
    def before(self):
        print('登录')

    @allure.step('测试查询订单')
    def test_001(self):
        self.before()
        print('查询订单')
