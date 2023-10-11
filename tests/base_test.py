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

        HOST_ALT_SERVER = os.getenv("HOST_ALT_SERVER")
        BITBAR_APIKEY = os.getenv("BITBAR_APIKEY")
        BITBAR_APP_ID_SDK_202_IPA = os.getenv("BITBAR_APP_ID_SDK_202_IPA")

        options = XCUITestOptions()
        options.platform_name = 'iOS'
        options.automation_name = "XCUITest"
        options.set_capability("deviceName", "Apple iPhone SE 2020 A2296 13.4.1")
        options.set_capability("appium:bundleId", "fi.altom.trashcat")
        options.set_capability("bitbar_apiKey", BITBAR_APIKEY)
        options.set_capability("bitbar_project", "client-side: AltServer on custom host; iOS")
        options.set_capability("bitbar_testrun", "Start Page Tests on Apple iPhone SE 2020 A2296 13.4.1")
        
        #See available devices at: https://cloud.bitbar.com/#public/devices
        options.set_capability("bitbar_device", "Apple iPhone SE 2020 A2296 13.4.1")
        options.set_capability("bitbar_app", BITBAR_APP_ID_SDK_202_IPA)
        time.sleep(15)

        cls.driver = webdriver.Remote(
            'http://localhost:4723/wd/hub', options=options)
        time.sleep(15)
        cls.altdriver = AltDriver(host=HOST_ALT_SERVER)

    @classmethod
    def tearDownClass(cls):
        cls.altdriver.stop()
        cls.driver.quit()
