from appium.webdriver import WebElement
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from apiV1 import API

# This example requires Selenium WebDriver 3.13 or newer
# geckodriver needs to be in path
ChromePath = r"C:\Users\X\Desktop\MyPFE\Framework Using Python\examples\Intellij-And-Gradle\src\chromedriver.exe"
driver = webdriver.Chrome(executable_path=ChromePath)
wait = WebDriverWait(driver, 10)
driver.get("https://www.seleniumeasy.com/test/basic-checkbox-demo.html")
api = API(driver)
api.activateChoice(By.CSS_SELECTOR, "div.checkbox:nth-child(3) > label:nth-child(1) > input:nth-child(1)")

# # driver.quit()

# with webdriver.Chrome(executable_path=ChromePath) as driver:
#     wait = WebDriverWait(driver, 10)
#     driver.get("https://google.com/ncr")
#     driver.find_element(By.NAME, "q").send_keys("cheese" + Keys.RETURN)
#     first_result = wait.until(presence_of_element_located((By.CSS_SELECTOR, "h3>div")))
#     print(first_result.get_attribute("textContent"))
#     driver.quit()
