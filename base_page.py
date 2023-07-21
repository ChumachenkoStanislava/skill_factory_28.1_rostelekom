from urllib.parse import urlparse
from time import sleep


class BasePage():
    def __init__(self, driver, url, timeout=5):
        self.driver = driver
        self.base_url = 'https://b2c.passport.rt.ru'
        self.driver.implicitly_wait(timeout)
        sleep(10)

    def get_base_url(self):
        url = urlparse(self.driver.current_url)
        return url.hostname

    def scroll_down(self, offset=0):

        if offset:
            self.driver.execute_script('window.scrollTo(0, {0});'.format(offset))
        else:
            self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    def scroll_up(self, offset=0):

        if offset:
            self.driver.execute_script('window.scrollTo(0, -{0});'.format(offset))
        else:
            self.driver.execute_script('window.scrollTo(0, -document.body.scrollHeight);')
