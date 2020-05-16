from selenium.common.exceptions import WebDriverException, NoSuchElementException


class API:
    def __init__(self, driver):
        self.driver = driver

    def __repr__(self):
        return '<{0.__module__}.{0.__name__} (session="{1}")>'.format(
            type(self), self._driver.session_id)

    def find_element(driver, by):
        """Looks up an element. Logs and re-raises ``WebDriverException``
        if thrown."""

        try:
            return driver.find_element(*by)
        except NoSuchElementException as e:
            raise e
        except WebDriverException as e:
            raise e

    def activateChoice(self, method, text):
        # The element to be selected need to be already visible in the page
        element = self.driver.find_element(method, text)  # errors are already handled by the find element driver method
        if (element.get_attribute('checked') == 'true'):  # depends on the app
            # print('element already selected')
            pass
        else:
            element.click()

    def deactivateChoice(self, method, text):
        element = self.driver.find_element(method, text)
        if (element.get_attribute('checked') == 'flase'):  # depends on the app
            # print('element already selected')
            pass
        else:
            element.click()
