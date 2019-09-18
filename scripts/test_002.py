import pytest, allure


class TestAllure:

    @allure.step('登录操作')
    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    def test_001(self):
        allure.attach('用户名', '13845612301')
        allure.attach('密码', '123456')
        assert True

    @allure.step('搜索商品操作')
    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    def test_002(self):
        assert True

    @allure.step('添加购物车操作')
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_003(self):
        assert True

    @allure.step('修改收货地址操作')
    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    def test_004(self):
        assert False

    @allure.step('修改商品数量操作')
    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    def test_005(self):
        assert True


