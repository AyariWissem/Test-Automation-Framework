Set up:
=======
there are many ways to use this script, using pycharm:
create a new folder in your pycharm project
right click on it > Mark Directory As > source root

Usage Example:
==============

#From the same project create a new python script and paste the code below

from apiV1 import API

caps = {
    "platformName": "Android",
    "platformVersion": "9",
    "deviceName": "Pixel3",
    "automationName": "UiAutomator2",
    "app": r"C:\Users\X\Desktop\MyPFE\Framework Using Python\Drivers&Apps\ApiDemos-debug.apk",
    "newCommandTimeout": 6000
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
driver.find_element(MobileBy.ACCESSIBILITY_ID, "Accessibility").click()
driver.find_element(MobileBy.ACCESSIBILITY_ID, "Accessibility Node Querying").click()
api = API(driver)
api.activateChoice(MobileBy.XPATH,
   "//android.widget.TextView[@text='Take out Trash']/following-sibling::android.widget.CheckBox")

