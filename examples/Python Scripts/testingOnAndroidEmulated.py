from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from apiV1 import API

caps = {
    "platformName": "Android",
    "platformVersion": "9",
    "deviceName": "Pixel3",
    "automationName": "UiAutomator2",
    "app": r"C:\Users\X\Desktop\MyPFE\Framework Using Python\Drivers&Apps\ApiDemos-debug.apk",
    "newCommandTimeout": 6000
}

# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
# def find_element(driver, by):
#   """Looks up an element. Logs and re-raises ``WebDriverException``
#   if thrown."""
#   try:
#     return driver.find_element(*by)
#   except NoSuchElementException as e:
#     raise e
#   except WebDriverException as e:
#     raise e


driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
driver.find_element(MobileBy.ACCESSIBILITY_ID, "Accessibility").click()
driver.find_element(MobileBy.ACCESSIBILITY_ID, "Accessibility Node Querying").click()
a = driver.find_element(MobileBy.XPATH,
                        "//android.widget.TextView[@text='Take out Trash']/following-sibling::android.widget.CheckBox")

api = API(driver)
api.activateChoice(MobileBy.XPATH,
                   "//android.widget.TextView[@text='Take out Trash']/following-sibling::android.widget.CheckBox")

# el1 = driver.find_element_by_accessibility_id("Accessibility")
# el1.click()
# el2 = driver.find_element_by_accessibility_id("Accessibility Node Querying")
# el2.click()
# el3 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.CheckBox")
# el3.click()
# el4 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[3]/android.widget.CheckBox")
# el4.click()
#
# driver.quit()
