from selenium.webdriver.support.wait import WebDriverWait


class API:
    def __version__(self):
        self.__version__ = "1.0.1"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
    def __repr__(self):
        return '<{0.__module__}.{0.__name__} (session="{1}")>'.format(
            type(self), self.driver.session_id)

    def activateChoice(self, locator, location):

        # The element to be selected needs to be already visible in the page
        element = self.driver.find_element(locator, location)
        # errors are already handled by the find element driver method
        state = element.is_selected()

        if state:
            # print('element already selected')
            pass
        else:
            element.click()

    def deactivateChoice(self, locator, location):
        element = self.driver.find_element(locator, location)
        state = element.is_selected()

        if not state:
            # print('element already deselected')
            pass
        else:
            element.click()


    def ElementsText(self,locator, location):
        element = self.driver.find_element(locator, location)
