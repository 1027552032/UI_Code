
import pytest
import os
import shutil
from playwright.sync_api import sync_playwright
import allure
from config.settings import Settings


def clean_reports():
    # 清理 Allure 报告目录
    if os.path.exists(Settings.ALLURE_RESULTS_DIR):
        shutil.rmtree(Settings.ALLURE_RESULTS_DIR)
    os.makedirs(Settings.ALLURE_RESULTS_DIR, exist_ok=True)
    
    if os.path.exists(Settings.ALLURE_REPORT_DIR):
        shutil.rmtree(Settings.ALLURE_REPORT_DIR)
    os.makedirs(Settings.ALLURE_REPORT_DIR, exist_ok=True)
    
    # 清理截图和视频目录
    if os.path.exists("screenshots"):
        shutil.rmtree("screenshots")
    os.makedirs("screenshots", exist_ok=True)
    
    if os.path.exists("videos"):
        shutil.rmtree("videos")
    os.makedirs("videos", exist_ok=True)


@pytest.fixture(scope="session", autouse=True)
def clean_old_reports():
    # 在测试会话开始前自动清理旧报告
    clean_reports()


@pytest.fixture(scope="session")
def browser_type():
    return Settings.BROWSER


@pytest.fixture(scope="session")
def browser(browser_type):
    with sync_playwright() as p:
        browser_type_map = {
            "chromium": p.chromium,
            "firefox": p.firefox,
            "webkit": p.webkit
        }
        browser = browser_type_map[browser_type].launch(
            headless=Settings.HEADLESS,
            slow_mo=Settings.SLOW_MO
        )
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser, request):
    context = browser.new_context(
        viewport={"width": 1920, "height": 1080},
        record_video_dir="videos/" if Settings.RECORD_VIDEO else None
    )
    page = context.new_page()
    page.set_default_timeout(Settings.DEFAULT_TIMEOUT)

    yield page

    if request.node.rep_call.failed if hasattr(request.node, 'rep_call') else False:
        screenshot = page.screenshot()
        allure.attach(screenshot, name="Failure Screenshot", attachment_type=allure.attachment_type.PNG)

    context.close()


@pytest.fixture
def login_page(page):
    from pages.login_page import LoginPage
    return LoginPage(page)


@pytest.fixture
def course_page(page):
    from pages.course_page import CoursePage
    return CoursePage(page)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)
