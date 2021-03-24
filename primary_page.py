from selenium.webdriver import ActionChains
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from driver_cr import SeleniumLibraryExt
from robot.libraries.BuiltIn import BuiltIn


# from selenium.webdriver.common.by import By


class PrimaryPage:

    def navigate_menu_submenu(self, menu, submenu):
        self.driver = SeleniumLibraryExt._driver()
        position = self.driver.find_element_by_xpath(
            f"//ul[@class='navigation menu']//li[contains(@class,'tier-1 element-')]/a[text()='{menu}']")
        ac = ActionChains(self.driver)
        ac.move_to_element(position).perform()
        self.driver.find_element_by_xpath(
            "//ul[@class='navigation menu']//ul[@class='subnav menu']//li[contains(@class,'tier-2 element-')]//a["
            f"text()='{submenu}']").click()

    def search(self, search_string):
        """
        Method used to search in the search bar of the site and press Enter to find results
        """
        self.driver = SeleniumLibraryExt._driver()
        search_bar = self.driver.find_element_by_name("q")
        search_bar.clear()
        search_bar.send_keys(search_string)
        search_bar.send_keys(Keys.RETURN)
