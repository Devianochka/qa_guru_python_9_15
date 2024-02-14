import pytest
import os
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from config import Settings
from megamarket_tests.controls import attach
from dotenv import load_dotenv


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(autouse=True)
def browser_settings():
    config = Settings()
    options = Options()

    driver_options = webdriver.ChromeOptions()

    if config.remote:
        login = os.getenv('LOGIN')
        password = os.getenv('PASSWORD')
        options.capabilities.update(config.selenoid_capabilities)
        driver = webdriver.Remote(
            command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
            options=options)
        browser.config.driver = driver

    driver_options.page_load_strategy = config.page_load_strategy
    browser.config.driver_options = driver_options
    browser.config.base_url = config.base_url
    browser.config.window_width = config.window_width
    browser.config.window_height = config.window_height

    yield

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
    browser.quit()
