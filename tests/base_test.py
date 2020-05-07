import os
import sys
import time

sys.path.append(os.path.dirname(__file__))

from altunityrunner import AltrunUnityDriver
import unittest
import pytest
import os
from appium import webdriver

class TestBase(unittest.TestCase):
    platform = None
    if os.getenv("APPIUM_PLATFORM", "Android") == 'Android':
        platform = 'android'
    else:
        platform = 'ios'

    @classmethod
    def setUpClass(cls):
        cls.desired_caps = {}
        cls.desired_caps['platformName'] = os.getenv('APPIUM_PLATFORM', 'Android')
        cls.desired_caps['deviceName'] = os.getenv('APPIUM_DEVICE', 'device')
        cls.desired_caps['app'] = os.getenv("APPIUM_APPFILE", "application.apk")
        cls.desired_caps['automationName'] = os.getenv('APPIUM_AUTOMATION', 'UIAutomator2')
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', cls.desired_caps)
        time.sleep(10)
        cls.altdriver = AltrunUnityDriver(cls.driver, cls.platform)

    @classmethod
    def tearDownClass(cls):
        cls.altdriver.stop()
        cls.driver.quit()