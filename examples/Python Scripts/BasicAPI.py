""""
Pour le next, je propre de préparer l’env avec python et tu prepare un readme avec tous les details et les étapes.
Et je propose de préparer quelque APIs de test :

    search_produt : qui permet d’ecrire un pattern dans un entry(similiare a javaEdit en java)
    activateChoice : permet d’activer/désactiver un entree checkbox.
"""


# SyntaxWishedFor
# test site: https://www.seleniumeasy.com/test/basic-checkbox-demo.html
from selenium.common.exceptions import WebDriverException, NoSuchElementException


class BasicAPI(object):
    def __init__(self, driver):
        self._driver = driver  # protected just because

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

    def activateChoice(self, LocatorTuple):
        # The element to be selected need to be already visible in the page
        return self.find_element(self.driver, LocatorTuple)

    #####     vvvvvvvvvvvvvvvvvvv deleted when finished vvvvvvvvvvvvvvvvvvv   #####
    """ An expectation for checking that an element is present on the DOM
    of a page. This does not necessarily mean that the element is visible.
    locator - used to find the element
    returns the WebElement once it is located
    """

    def __init__(self, locator):
        self.locator = locator

    def __call__(self, driver):
        return _find_element(driver, self.locator).click()

    def _find_element(driver, by):
        """Looks up an element. Logs and re-raises ``WebDriverException``
        if thrown."""
        try:
            return driver.find_element(*by)
        except NoSuchElementException as e:
            raise e
        except WebDriverException as e:
            raise e

    # ##############################
    # def until(self, method, message=''):
    #     """Calls the method provided with the driver as an argument until the \
    #     return value is not False."""
    #     screen = None
    #     stacktrace = None
    #
    #     end_time = time.time() + self._timeout
    #     while True:
    #         try:
    #             value = method(self._driver)
    #             if value:
    #                 return value
    #         except self._ignored_exceptions as exc:
    #             screen = getattr(exc, 'screen', None)
    #             stacktrace = getattr(exc, 'stacktrace', None)
    #         time.sleep(self._poll)
    #         if time.time() > end_time:
    #             break
    #     raise TimeoutException(message, screen, stacktrace)
