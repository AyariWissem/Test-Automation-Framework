import time
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
#Test Description: This test
#These are my credentials if you want to try it
userName = "#"
accessKey = "#"

desired_cap = {
  "realMobile": "true",
  "project": "My First Project",
  "build": "My First Build",
  "name": "Wissem Python on browser stack"
}

def Android(desired_cap):
    desired_cap['device'] = 'Samsung Galaxy S10e'
    desired_cap['os_version'] = '9.0'
    desired_cap['app'] = 'bs://415f07ffce03895ff9f71c1e113a1dca1e40a99e'
    # desired_cap['browserName'] = 'Chrome'


def iOS(desired_cap):
    desired_cap['device'] = 'iPhone 11 Pro Max'
    desired_cap['os_version'] = '13'
    desired_cap['app'] = 'bs://40b157b3a53610e21aedb6f41b39adb7fa506180'
    # desired_cap['browserName'] = 'Safari'

class TestGmailTest():
    def setup_method(self, method):
        # iOS(desired_cap)
        Android(desired_cap)
        self.driver = webdriver.Remote("http://" + userName + ":" + accessKey + "@hub-cloud.browserstack.com/wd/hub",
                                  desired_cap)
        self.wait = WebDriverWait(self.driver,10)


    def teardown_method(self, method):
        self.driver.quit()

    def test_testCase1(self):

        self.wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, "Login Screen"))).click()
        self.driver.back()
        self.wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, "Webview Demo"))).click()
        time.sleep(2)
        nativeSource=self.driver.page_source
        Contexts = self.driver.contexts
        print("the available contexts are:\n"+Contexts);

        try:
            webview = Contexts[1]
            self.driver.switch_to.context(webview)
            print("changed to the context: " + webview)
            websource = self.driver.page_source
            self.driver.get("https://cloudgrey.io")
            webSource=self.driver.page_source
            # assert self.driver.title=="Cloud Grey: Appium Delivered")
            print(self.driver.contexts)

            assert self.driver.title=="Cloud Grey: Appium Delivered"

        except AssertionError as error:
            print("Failed to change to the webview context \n"+error)

