import allure
import pytest

class TestSetting:

    @allure.severity("blocker")
    @allure.step(title="用于测试“XXX”功能的测试脚本")
    def test_login1(self):
        print("");
        assert 1

    @allure.severity("critical")
    @allure.step(title="用于测试“XXXX”功能的测试脚本")
    def test_login2(self):
        print("");
        assert 1

    @allure.severity("normal")
    @allure.step(title="用于测试“XXXX”功能的测试脚本")
    def test_login3(self):
        print("");
        assert 1

    #默认就是"normal"级别，即相当于：@allure.severity("normal")
    @allure.step(title="用于测试“XXXX”功能的测试脚本")
    def test_login4(self):
        print("");
        assert 1

    @allure.severity("minor")
    @allure.step(title="用于测试“XXXX”功能的测试脚本")
    def test_login5(self):
        print("");
        assert 1

    @allure.severity("trivial")
    @allure.step(title="用于测试“XXXX”功能的测试脚本")
    def test_login6(self):
        print("");
        assert 1
