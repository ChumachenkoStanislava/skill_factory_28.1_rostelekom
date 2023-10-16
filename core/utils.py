from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


def get_chrome():
    return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


def get_firefox():
    return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))