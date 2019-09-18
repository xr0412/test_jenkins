import pytest, allure


class TestSeverity:

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    def test_001(self):
        assert True

    @allure.step("注册操作")
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_002(self):
        assert False

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    def test_003(self):
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    def test_004(self):
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    def test_005(self):
        assert True
