# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains
# from selenium.webdriver.chrome.options import Options
from functools import wraps
from driver_cr import SeleniumLibraryExt
from robot.libraries.BuiltIn import BuiltIn


def decorator_driver_quit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        driver = func(*args, **kwargs)
        print("Process executed!")
        driver.close()
        print("Driver was stopped successfully!")

    return wrapper


class DecoratorPage:



    def open_content_examples(self):
        """
        Method used to click on the Examples submenu from the Contents menu
        """
        self.driver = SeleniumLibraryExt._driver()
        content_view = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//article[@class='text']")))
        content_view_example = content_view.find_element_by_xpath("//ul[@class='simple']//a[text()='Examples']")
        ac2 = ActionChains(self.driver)
        ac2.move_to_element(content_view_example).click(content_view_example).perform()

    def verify_example_count(self):
        """
        Verify the number of examples presented in the Examples paragraph of the page
        :return: True if the number of examples in the Example sections is 5, False otherwise
        """
        self.driver = SeleniumLibraryExt._driver()
        self.open_content_examples()
        examples_view = self.driver.find_element_by_xpath("//div[@id='examples']//ol[@class='arabic']")
        examples_list = examples_view.find_elements_by_tag_name("li")
        if len(examples_list) == 5:
            print("Yes, there are {} examples".format(str(len(examples_list))))

        else:
            print("No, there are {} examples".format(str(len(examples_list))))
        # return self.driver
