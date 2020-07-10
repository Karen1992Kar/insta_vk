
import pytest
from selenium import webdriver


@pytest.fixture
def browser():
    download_dir = 'C:\\Users\\Karen\\Desktop\\insta_vk\\pages\\'

    chrome_options = webdriver.ChromeOptions()

    profile = {"plugins.plugins_list": [{"enabled": False, "name": "Chrome PDF Viewer"}],
               "download.default_directory": download_dir,
               "download.extensions_to_open": "applications/pdf"}
    chrome_options.add_experimental_option("prefs", profile)

    browser = webdriver.Chrome(chrome_options=chrome_options)
    yield browser
    browser.quit()
