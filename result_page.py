# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains
from driver_cr import SeleniumLibraryExt
from robot.libraries.BuiltIn import BuiltIn


# from selenium.webdriver.chrome.options import Options
# from functools import wraps

class ResultPage:



    def get_first_result(self, result):
        """
        Method used to click on the first result from the search list
        """
        self.driver = SeleniumLibraryExt._driver()
        results_view = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//ul[@class='list-recent-events "
                                                      "menu']")))
        first_result = results_view.find_element_by_xpath(
            f"//a[text()='{result}']")
        ac = ActionChains(self.driver)
        ac.move_to_element(first_result).click(first_result).perform()
