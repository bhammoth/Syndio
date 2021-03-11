from selenium import webdriver
import re

from selenium.webdriver.firefox.options import Options

from test.TestBase import TestBase


# UI design spec test
class UiDesignTest(TestBase):

    def setUp(self):
        options = Options()
        options.binary_location = TestBase.firefox_binary_location
        self.driver = webdriver.Firefox(options=options)

    def test_gender_active_button_tab(self):
        # setup, openurl
        driver = self.driver
        driver.get(TestBase.app_base_url)
        driver.implicitly_wait(10)

        gender_button = driver.find_element_by_id("tab-gender").find_element_by_tag_name("button")
        height = gender_button.value_of_css_property("height")  # 40px
        width = gender_button.value_of_css_property("width")  # 200px
        bg_color = gender_button.value_of_css_property("background-color")  # D8D8D8
        r, g, b = map(int, re.search(
            r'rgb\((\d+),\s*(\d+),\s*(\d+)', bg_color).groups())
        hex_bg_color = '#%02x%02x%02x' % (r, g, b)

        font_size = gender_button.value_of_css_property("font-size")  # 14pt
        text_color = gender_button.value_of_css_property("color")  # 2E2E2E
        r, g, b = map(int, re.search(
            r'rgb\((\d+),\s*(\d+),\s*(\d+)', text_color).groups())
        hex_text_color = '#%02x%02x%02x' % (r, g, b)
        font_size_float = int(float(font_size[0:-2]) * 72 / 96)
        self.assertEqual(
            (height, width, hex_bg_color.upper(), hex_text_color.upper(), str(font_size_float) + "pt"),
            ("40px", "200px", "#D8D8D8", "#2E2E2E", "14pt"))

    def tearDown(self):
        self.driver.close()
