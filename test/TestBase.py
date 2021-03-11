from selenium import webdriver
import unittest


class TestBase(unittest.TestCase):
    mock_base_url = "https://run.mocky.io"
    group_by_function_id = "a9f6a4b7-d03c-4a45-b64b-791e054f36b8"
    group_by_role_id = "f1b01b57-3147-476a-a632-0c10ad2a3c1a"
    group_names_and_ids = "9e343425-c47c-4c7f-a1ac-972c099be0ed"
    version = "/v3/"
    base_version_url = mock_base_url + version
    mock_base_url = "https://run.mocky.io"
    app_base_url = "https://syndio-dashboard.herokuapp.com"
    tab_inactive = "tab-inactive"
    tab_active = "tab-active"
    firefox_binary_location = "/Applications/Browsers/Firefox.app/Contents/MacOS/firefox-bin"
