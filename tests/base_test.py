from unittest import TestCase
from alttester import AltDriver
from appium import webdriver
from appium.options.common import AppiumOptions
import os
import sys
import time

sys.path.append(os.path.dirname(__file__))


class TestBase(TestCase):
    platform = None

    @classmethod
    def setUpClass(cls):

        options = AppiumOptions()
        options.platform_name = 'Android'
        options.automation_name = "UiAutomator2"
        options.set_capability("app", os.path.abspath("application.apk"))

        time.sleep(15)

        cls.driver = webdriver.Remote(
            'http://localhost:4723/wd/hub', options=options)
        time.sleep(15)
        cls.altdriver = AltDriver()

    @classmethod
    def tearDownClass(cls):
        cls.altdriver.stop()
        cls.driver.quit()
