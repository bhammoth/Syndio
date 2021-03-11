from selenium import webdriver
import unittest

from selenium.webdriver.firefox.options import Options

from test.TestBase import TestBase


class UiTest(TestBase):

    def setUp(self):
        options = Options()
        options.binary_location = TestBase.firefox_binary_location
        self.driver = webdriver.Firefox(options=options)

    def test_race_gender_toggle(self):
        driver = self.driver
        driver.get(TestBase.app_base_url)
        driver.implicitly_wait(10)
        button = driver.find_element_by_id("tab-race")
        button.click()

    def test_gender_toggle_default(self):
        driver = self.driver
        driver.get(TestBase.app_base_url)
        driver.implicitly_wait(10)
        gender_button = driver.find_element_by_id("tab-gender").find_element_by_tag_name("button")
        gender_button_class_names = gender_button.get_attribute("class")
        self.assertIn(TestBase.tab_active, gender_button_class_names)

    def test_race_gender_toggle_isInactive(self):
        driver = self.driver
        driver.get(TestBase.app_base_url)
        driver.implicitly_wait(10)
        race_button = driver.find_element_by_id("tab-race").find_element_by_tag_name("button")
        gender_button = driver.find_element_by_id("tab-gender").find_element_by_tag_name("button")

        race_button_class_names = race_button.get_attribute("class")
        gender_button_class_names = gender_button.get_attribute("class")

        self.assertIn(TestBase.tab_inactive, race_button_class_names)
        self.assertIn(TestBase.tab_active, gender_button_class_names)

        race_button.click()

        race_button_class_names = race_button.get_attribute("class")
        gender_button_class_names = gender_button.get_attribute("class")

        self.assertIn(TestBase.tab_inactive, gender_button_class_names)
        self.assertIn(TestBase.tab_active, race_button_class_names)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
