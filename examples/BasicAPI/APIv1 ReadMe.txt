Setup instructions:
===================
there are many ways to use this script, using pycharm:
create a new folder in your pycharm project
right click on the folder> Mark Directory As > Sources Root

Usage in your test script:
=========================
# The module import
from apiV1 import API


#Instantiation using your webdriver object that should already be created
api = API(driver)

# Api method usage
# api.activateChoice(locator, Location)
# locator = By.ID, By.CSS_SELECTOR, MobileBy.XPATH .....
# location = xpath,..
# Example:
api.activateChoice(MobileBy.XPATH,
   "//android.widget.TextView[@text='Take out Trash']/following-sibling::android.widget.CheckBox")

