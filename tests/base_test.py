from unittest import TestCase
from alttester import AltDriver
from appium import webdriver
from appium.options.ios import XCUITestOptions
import os
import sys
import time

sys.path.append(os.path.dirname(__file__))


class TestBase(TestCase):
    platform = None

    @classmethod
    def setUpClass(cls):

        options = XCUITestOptions()
        options.platform_name = 'iOS'
        options.automation_name = "XCUITest"
        options.set_capability("appium:deviceName", "Apple iPhone SE 2020 A2296 13.4.1")
        options.set_capability("appium:bundleId", "fi.altom.trashcat")
        options.set_capability("platformVersion", "13.4")
        options.set_capability("autoAcceptAlerts", "true")
        options.set_capability("newCommandTimeout", 2000)
        
        time.sleep(15)

        cls.driver = webdriver.Remote(
            'http://localhost:4723/wd/hub', options=options)
        time.sleep(15)
        cls.altdriver = AltDriver(host="INSERT_VM_IP")

    @classmethod
    def tearDownClass(cls):
        cls.altdriver.stop()
        cls.driver.quit()
