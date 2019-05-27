import allure,pytest


class Test_001:
    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step(title="这是一个测试报告01")
    def test_001(self):
        print("--test001--")
        allure.attach("标题","具体内容")
        assert True