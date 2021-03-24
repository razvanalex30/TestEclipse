from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import re


class VersionRetrieve:
    """
    Class used to retrieve the last Python Version from Python's official website
    """

    def __init__(self):
        self.driver = None
        self.first_release = None
        self.last_active_version = None

    @staticmethod
    def date_parse_2(input_str):
        date_obj = datetime.strptime(input_str, "%Y-%m-%d")
        return date_obj

    @staticmethod
    def date_parse(input_str):
        date_string = input_str.split(" ")
        final_date = " ".join([date_string[0][0:3], date_string[1], date_string[2]])
        date_obj = datetime.strptime(final_date, "%b %d, %Y")
        return date_obj

    @staticmethod
    def string_parse(input_str):
        """
        Method used to retrieve the Python Version
        :param input_str: Python Version string obtained from the site
        :return: Retains only the version number
        """
        version_number = re.findall(r'[0-9]+.[0-9]+.[0-9]+', input_str)
        return version_number[0]

    def navigate(self):
        """
        Method used to start a Chrome Websession and navigate to Python's Official Website
        :return: driver, necessary for completing other tasks on the webpage
        """
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome('C:/Users/RAlexandru/Documents/Proiecte Eclipse/tesv2/chromedriver.exe', options=chrome_options)
        self.driver.get('https://www.python.org/')

    def find_path(self):
        """
        Method used to find the path to Downloads -> All releases menu
        """
        self.navigate()
        menu = self.driver.find_element_by_xpath(
            "//ul[@class='navigation menu']//li[contains(@class,'tier-1 element-')]/a[text()='Downloads']")
        ac = ActionChains(self.driver)
        ac.move_to_element(menu).perform()
        self.driver.find_element_by_xpath(
            "//ul[@class='navigation menu']//ul[@class='subnav menu']//li[contains(@class,'tier-2 element-')]//a["
            "text()='All releases']").click()

    def retrieve_version(self):
        """
        Method used to retrieve the last python version from the table available in All releases
        """
        self.find_path()
        self.retrieve_table_version()
        all_releases = self.driver.find_element_by_xpath("//*[@id='content']/div/section/div[2]/ol")
        versions = all_releases.find_elements_by_tag_name("li")
        release_list = []
        for version in versions:
            version_dict = {'release_version': None, 'release_date': None}
            header = version.find_element_by_class_name("release-number")
            header_2 = version.find_element_by_class_name("release-date")
            version_dict['release_version'] = self.string_parse(header.text)
            version_dict['release_date'] = self.date_parse(header_2.text)
            if version_dict['release_date'] > self.first_release:
                if self.last_active_version in version_dict['release_version']:
                    release_list.append(version_dict)
        if len(release_list) > 0:
            print("Yes, there are {} versions newer than the {} version".format(len(release_list),
                                                                                self.last_active_version))
            print("The versions are:")
            for elem in release_list:
                print(str(elem['release_version']) + " released on: " + elem['release_date'].strftime("%Y-%b-%d"))
        else:
            print("There are no versions newer than the {} version".format(self.last_active_version))

    def retrieve_table_version(self):
        last_python_version = self.driver.find_element_by_xpath("//ol[@class='list-row-container menu']//li//span["
                                                                "text()='3.9']")
        last_active_version = last_python_version.text
        self.last_active_version = last_active_version
        release_active_version = self.driver.find_element_by_xpath("//ol[@class='list-row-container menu']//li//span["
                                                                   "text()='2020-10-05']")
        header = release_active_version.text
        first_release = self.date_parse_2(header)
        self.first_release = first_release


version_last = VersionRetrieve()
version_last.retrieve_version()
