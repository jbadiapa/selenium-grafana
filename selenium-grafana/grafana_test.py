import unittest
from selenium import webdriver
# from selenium.webdriver.common.by import By
from time import sleep


class GrafanaSelenium(unittest.TestCase):

    def setUp(self):
        profile = webdriver.FirefoxProfile()
        profile.set_preference('network.http.phishy-userpass-length', 255)
        self.driver = webdriver.Firefox(firefox_profile=profile)
        self.username = 'admin'
        self.password = 'admin'
        self.ip = '192.168.33.51'
        self.url = 'https://{}/grafana/'.format(self.ip)

    def _url_load(self, url):
        driver = self.driver
        driver.get(url)
        sleep(2)
        return driver

    def _url_test(self, url, text):
        driver = self._url_load(url)
        assert text in driver.title
        return driver

    def test_grafana_login_page(self):
        return self._url_test(self.url, 'Grafana')

    def test_grafana_login(self):
        driver = self.test_grafana_login_page()
        # Find needed elements
        user = driver.find_element_by_name('username')
        passw = driver.find_element_by_id('inputPassword')
        button = driver.find_element_by_class_name('btn-inverse')
        # Insert the login data
        user.send_keys(self.username)
        passw.send_keys(self.password)
        # click the login button
        button.click()
        sleep(1)
        assert 'Grafana - Home' in driver.title

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
