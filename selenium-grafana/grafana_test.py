import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep
import sys


class GrafanaSelenium(unittest.TestCase):

    USERNAME = 'admin'
    PASSWORD = 'admin'
    PROTOCOL = 'https'
    PORT = 443
    IP = 'localhost'

    def setUp(self):
        caps = DesiredCapabilities.CHROME.copy()
        caps['acceptInsecureCerts'] = True
        caps['level'] = 'trace'
        self.driver = webdriver.Chrome(desired_capabilities=caps)
        self.url = '{protocol}://{ip}:{port}/grafana/'.format(
            protocol=GrafanaSelenium.PROTOCOL,
            ip=GrafanaSelenium.IP,
            port=GrafanaSelenium.PORT)

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
        user.send_keys(GrafanaSelenium.USERNAME)
        passw.send_keys(GrafanaSelenium.PASSWORD)
        # click the login button
        button.click()
        sleep(2)
        assert 'Grafana - Home' in driver.title

    def tearDown(self):
        self.driver.close()


def parse_argument():
    arguments = {'--ip': 'localhost',
                 '--protocol': 'https',
                 '--username': 'admin',
                 '--password': 'admin',
                 '--port': '443'}
    iterations = list(sys.argv)
    for arg in iterations:
        if arg in arguments.keys():
            pos = sys.argv.index(arg)
            sys.argv.pop(pos)
            arguments[arg] = sys.argv.pop(pos)

    GrafanaSelenium.USERNAME = arguments['--username']
    GrafanaSelenium.PASSWORD = arguments['--password']
    GrafanaSelenium.IP = arguments['--ip']
    GrafanaSelenium.PROTOCOL = arguments['--protocol']
    GrafanaSelenium.PORT = arguments['--port']


if __name__ == "__main__":
    parse_argument()
    unittest.main()
