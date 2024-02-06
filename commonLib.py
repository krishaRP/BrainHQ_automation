from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains


# Create a commonLib class with selenium webdriver
# All the methods are find, wait_for to be used in the pages like Auth/Privacy
class CommonLib:

    def __init__(self, driver):
        self.driver = driver
        self._wait = WebDriverWait(self.driver, 10)
        self._action = ActionChains(self.driver)

    def wait_for(self, locator):
        return self._wait.until(ec.presence_of_element_located(locator))

    def maximize(self):
        return self.driver.maximize_window()

    def find(self, locator):
        return self.driver.find_element(*locator)

    def context_click(self, element):
        return self._action.context_click(element)

    def alert(self):
        return self._wait.until(ec.alert_is_present())