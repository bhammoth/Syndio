import requests
from selenium import webdriver
import unittest
import json

from selenium.webdriver.firefox.options import Options

from test.TestBase import TestBase


class FlowsTest(TestBase):

    def setUp(self):
        options = Options()
        options.binary_location = TestBase.firefox_binary_location
        self.driver = webdriver.Firefox(options=options)

    def test_e2e_minority_values_group_by_function(self):
        # setup, openurl
        driver = self.driver
        driver.get(TestBase.app_base_url)
        driver.implicitly_wait(10)

        # get minority value from UI->API call to group mock->getFunctionId -> make api call to function mock -> get
        # minority value from mock
        ui_minortiy_value = driver.find_element_by_id("payEquityGap").find_element_by_tag_name("strong").text
        group_name_url = TestBase.base_version_url + TestBase.group_names_and_ids
        function_id = requests.get(group_name_url).json()[0]['id']
        function_url = TestBase.base_version_url + function_id
        mock_minortiy_value = requests.get(function_url).json()[
            'data']['gender']['payEquityGap']['data']['minority']['value']

        # assert mock api and iu values are equal
        self.assertEqual(ui_minortiy_value, mock_minortiy_value)

    def test_e2e_employee_comparison_group_by_function(self):
        # setup, openurl
        driver = self.driver
        driver.get(TestBase.app_base_url)
        driver.implicitly_wait(10)

        # get comparison value from UI->API call to group mock->getFunctionId -> make api call to function mock -> get
        # comparison value from mock
        ui_comparison_value = driver.find_element_by_id("employeeComparison").find_element_by_tag_name("strong").text
        group_name_url = TestBase.base_version_url + TestBase.group_names_and_ids
        function_id = requests.get(group_name_url).json()[0]['id']
        function_url = TestBase.base_version_url + function_id
        mock_comparison_value = requests.get(function_url).json()[
            'data']['gender']['employeeComparison']['data']['value']
        # assert mock api and iu values are equal
        self.assertEqual(ui_comparison_value, mock_comparison_value)

    def test_e2e_employee_comparison_group_by_functionv(self):
        driver = self.driver
        driver.get(TestBase.app_base_url + "/?" + TestBase.group_by_function_id)
        driver.implicitly_wait(10)

        # get comparison value from UI->API call to group mock->getFunctionId -> make api call to function mock -> get
        # comparison value from mock
        ui_comparison_value = driver.find_element_by_id("employeeComparison").find_element_by_tag_name("strong").text
        group_name_url = TestBase.base_version_url + TestBase.group_names_and_ids
        function_id = requests.get(group_name_url).json()[0]['id']
        function_url = TestBase.base_version_url + function_id
        mock_comparison_value = requests.get(function_url).json()[
            'data']['gender']['employeeComparison']['data']['value']
        # assert mock api and iu values are equal
        self.assertEqual(ui_comparison_value, mock_comparison_value)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
