from alttester import AltDriver, AltPortForwarding
from appium import webdriver
from unittest import TestCase
import os
import sys
import time

sys.path.append(os.path.dirname(__file__))


class TestBase(TestCase):
    platform = None

    @classmethod
    def setUpClass(cls):
        if os.getenv("APPIUM_PLATFORM", "android") == 'android':
            cls.platform = 'android'
        else:
            cls.platform = 'ios'
        print("Running on " + cls.platform)
        cls.desired_caps = {}
        cls.desired_caps['platformName'] = os.getenv(
            'APPIUM_PLATFORM', 'Android')
        cls.desired_caps['deviceName'] = os.getenv('APPIUM_DEVICE', 'device')
        cls.desired_caps['app'] = os.getenv(
            "APPIUM_APPFILE", "TrashCat.apk")
        cls.desired_caps['automationName'] = os.getenv(
            'APPIUM_AUTOMATION', 'UIAutomator2')
        cls.driver = webdriver.Remote(
            'http://localhost:4723/wd/hub', cls.desired_caps)
        print("Appium driver started")
        time.sleep(10)
        cls.setup_port_forwarding()
        cls.altdriver = AltDriver()

    @classmethod
    def setup_port_forwarding(cls):
        try:
            AltPortForwarding.remove_all_forward_android()
        except:
            print("No adb forward was present")
        try:
            AltPortForwarding.kill_all_iproxy_process()
        except:
            print("No iproxy forward was present")

        if cls.platform == 'android':
            AltPortForwarding.forward_android()
            print("Port forwarded (Android).")
        else:
            AltPortForwarding.forward_ios()
            print("Port forwarded (iOS).")

    @classmethod
    def tearDownClass(cls):
        cls.altdriver.stop()
        cls.driver.quit()
