from browser import Browser
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class GrafanaSelenium(unittest.TestCase):

    def setUp(self):
        browser.start()

    def _url_load(self, url):
        browser.load_page_site(url)
        return browser.driver

    def _url_test(self, url, text):
        driver = self._url_load(url)
        assert text in driver.title
        return driver

    def test_grafana_login_page(self):
        return self._url_test('', 'Grafana')

    def test_grafana_login(self):
        self.test_grafana_login_page()
        # Find needed elements
        user = browser.wait_for_obj(EC.presence_of_element_located(
            (By.NAME, 'username')
        ))

        passw = browser.wait_for_obj(EC.presence_of_element_located(
            (By.ID, 'inputPassword')
        ))
        button = browser.wait_for_obj(EC.presence_of_element_located(
            (By.CLASS_NAME, 'btn-inverse')
        ))
        # Insert the login data
        user.send_keys(browser.username)
        passw.send_keys(browser.password)
        # click the login button
        button.click()
        browser.wait_for_obj(EC.title_is('Grafana - Home'))

    def tearDown(self):
        browser.end()


if __name__ == "__main__":
    browser = Browser(screenshot_on_error=True)
    browser.parse_arguments()
    browser.set_url('grafana/')
    unittest.main()
