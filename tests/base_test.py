import os
import sys

sys.path.append(os.path.dirname(__file__))

from altunityrunner import AltrunUnityDriver
import unittest
import pytest
import os
from appium import webdriver

class TestBase(unittest.TestCase):
    plaform = os.getenv('TESTS_PLATFORM', 'android')

    @classmethod
    def setUpClass(cls):
        cls.desired_caps = {}
        cls.desired_caps['platformName'] = 'Android'
        cls.desired_caps['deviceName'] = 'device'
        cls.desired_caps['app'] = os.getenv("APPIUM_APPFILE", "application.apk")
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', cls.desired_caps)

        cls.altdriver = AltrunUnityDriver(cls.driver, cls.plaform)

    @classmethod
    def tearDownClass(cls):
        cls.altdriver.stop()
        cls.driver.quit()