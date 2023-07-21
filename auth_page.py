from base_page import BasePage
from selenium.webdriver.common.by import By
from urllib.parse import urlparse


class AuthForm(BasePage):
    def __init__(self, driver, timeout=10, ):
        super().__init__(driver, timeout)
        url = 'https://b2c.passport.rt.ru'
        driver.get(url)

        self.username = driver.find_element(By.ID, "username")
        self.password = driver.find_element(By.ID, "password")
        self.auth_btn = driver.find_element(By.ID, "kc-login")
        self.forgot = driver.find_element(By.ID, "forgot_password")
        self.register = driver.find_element(By.ID, 'kc-register')
        self.placeholder = driver.find_element(By.XPATH,
                                               '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]')
        self.agree = driver.find_element(By.ID, "rt-footer-agreement-link")
        self.vk_btn = driver.find_element(By.ID, "oidc_vk")
        self.ok_btn = driver.find_element(By.ID, 'oidc_ok')
        self.mailru_btn = driver.find_element(By.ID, 'oidc_mail')
        self.ya_btn = driver.find_element(By.ID, 'oidc_ya')

    def find_other_element(self, by, location):
        return self.driver.find_element(by, location)

    def btn_click(self):
        self.auth_btn.click()

    def get_current_url(self):
        url = urlparse(self.driver.current_url)
        return url.path
