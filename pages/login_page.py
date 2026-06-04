
import allure
from pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME_INPUT = 'input[placeholder="用户名"]'
    PASSWORD_INPUT = 'input[placeholder="密码"]'
    LOGIN_BUTTON = 'button:has-text("登录")'
    WELCOME_MESSAGE = 'text=欢迎'

    @allure.step("Enter username: {username}")
    def enter_username(self, username: str):
        self.fill(self.USERNAME_INPUT, username)

    @allure.step("Enter password")
    def enter_password(self, password: str):
        self.fill(self.PASSWORD_INPUT, password)

    @allure.step("Click login button")
    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    @allure.step("Perform login")
    def login(self, username: str, password: str):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    @allure.step("Verify login success")
    def verify_login_success(self):
        self.page.wait_for_url("**/mgr/**", timeout=15000)
        self.page.wait_for_load_state("networkidle")
