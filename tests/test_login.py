
import pytest
import allure
from config.settings import Settings


@allure.feature("User Login Module")
@allure.story("Login Functionality")
class TestLogin:

    @allure.title("Test successful login")
    @allure.description("Login with valid username and password, verify success")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_login_success(self, login_page):
        with allure.step("Step 1: Open login page"):
            login_page.open(Settings.LOGIN_URL)

        with allure.step("Step 2: Enter valid credentials and login"):
            login_page.login(Settings.USERNAME, Settings.PASSWORD)

        with allure.step("Step 3: Verify login success"):
            login_page.verify_login_success()
