import allure


class Test001:

    @allure.step('测试操作')
    def test_001(self):
        allure.attach('文本', '文本内容')
        assert True
