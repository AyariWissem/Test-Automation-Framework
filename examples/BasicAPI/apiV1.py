from selenium.common.exceptions import WebDriverException, NoSuchElementException


class API:
    def __init__(self, driver):
        self.driver = driver

    def __repr__(self):
        return '<{0.__module__}.{0.__name__} (session="{1}")>'.format(
            type(self), self._driver.session_id)

    def activateChoice(self, locator, location):
        # The element to be selected need to be already visible in the page
        element = self.driver.find_element(locator, location)  # errors are already handled by the find element driver method
        state=element.is_selected()
        if (state == True ):
            # print('element already selected')
            pass
        else:
            element.click()

    def deactivateChoice(self, locator, location):
        element = self.driver.find_element(locator, location)
        state = element.is_selected()
        if (state == False ):
            # print('element already deselected')
            pass
        else:
            element.click()
