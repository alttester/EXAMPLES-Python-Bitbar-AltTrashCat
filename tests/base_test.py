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

        HOST_ALT_SERVER = os.getenv("HOST_ALT_SERVER")
        BITBAR_APIKEY = os.getenv("BITBAR_APIKEY")
        BITBAR_APP_ID_SDK_202 = os.getenv("BITBAR_APP_ID_SDK_202")

        options = AppiumOptions()
        options.platform_name = 'Android'
        options.automation_name = "UiAutomator2"
        options.set_capability("bitbar_apiKey", BITBAR_APIKEY)
        options.set_capability("bitbar_project", "client-side: AltServer on custom host; Android")
        options.set_capability("bitbar_testrun", "Start Page Tests on Samsung")
        options.set_capability("app", os.path.abspath("application.apk"))
        
        #See available devices at: https://cloud.bitbar.com/#public/devices
        options.set_capability("bitbar_device", "Samsung Galaxy A52 -US")
        options.set_capability("bitbar_app", BITBAR_APP_ID_SDK_202)
        time.sleep(15)

        cls.driver = webdriver.Remote(
            'http://localhost:4723/wd/hub', options=options)
        time.sleep(15)
        cls.altdriver = AltDriver(host=HOST_ALT_SERVER)

    @classmethod
    def tearDownClass(cls):
        cls.altdriver.stop()
        cls.driver.quit()
