
from playwright.sync_api import Page, expect
import allure


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.timeout = 10000

    @allure.step("Open page: {url}")
    def open(self, url: str):
        self.page.goto(url, wait_until="networkidle")

    @allure.step("Click element: {selector}")
    def click(self, selector: str):
        self.page.locator(selector).click(timeout=self.timeout)

    @allure.step("Fill text: {text} into {selector}")
    def fill(self, selector: str, text: str):
        self.page.locator(selector).fill(text)

    @allure.step("Get element text: {selector}")
    def get_text(self, selector: str) -> str:
        return self.page.locator(selector).inner_text()

    @allure.step("Wait for element visible: {selector}")
    def wait_for_visible(self, selector: str):
        self.page.locator(selector).wait_for(state="visible", timeout=self.timeout)

    @allure.step("Assert element visible: {selector}")
    def assert_visible(self, selector: str):
        expect(self.page.locator(selector)).to_be_visible()

    @allure.step("Assert page title contains: {title}")
    def assert_title_contains(self, title: str):
        expect(self.page).to_have_title(title)

    @allure.step("Assert element text equals: {text}")
    def assert_text_equals(self, selector: str, text: str):
        expect(self.page.locator(selector)).to_have_text(text)

    def take_screenshot(self, name: str = "screenshot"):
        screenshot = self.page.screenshot()
        allure.attach(screenshot, name=name, attachment_type=allure.attachment_type.PNG)
