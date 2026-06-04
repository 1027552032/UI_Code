
import os


class Settings:
    ENV = os.getenv("TEST_ENV", "test")
    BASE_URL = os.getenv("BASE_URL", "http://121.43.36.83:7081")

    BROWSER = os.getenv("BROWSER", "chromium")
    HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
    SLOW_MO = int(os.getenv("SLOW_MO", "0"))

    DEFAULT_TIMEOUT = int(os.getenv("DEFAULT_TIMEOUT", 10000))
    IMPLICIT_WAIT = int(os.getenv("IMPLICIT_WAIT", 5))

    RECORD_VIDEO = os.getenv("RECORD_VIDEO", "true").lower() == "true"
    RECORD_TRACE = os.getenv("RECORD_TRACE", "false").lower() == "true"

    ALLURE_RESULTS_DIR = "reports/allure_results"
    ALLURE_REPORT_DIR = "reports/allure_report"

    LOGIN_URL = BASE_URL + "/mgr/login/login.html"
    USERNAME = "auto"
    PASSWORD = "sdfsdfsdf"
