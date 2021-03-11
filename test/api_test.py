import unittest

import requests

from test.TestBase import TestBase


# Contract Test
class ApiTest(TestBase):

    def test_get_names_and_ids(self):
        api_url = TestBase.base_version_url + TestBase.group_names_and_ids
        response_code = requests.get(api_url).status_code
        self.assertEqual(response_code, 200)

    def test_get_group_by_role_id(self):
        api_url = TestBase.base_version_url + TestBase.group_by_role_id
        response_code = requests.get(api_url).status_code
        self.assertEqual(response_code, 200)

    def test_get_group_by_function_id(self):
        api_url = TestBase.base_version_url + TestBase.group_by_function_id
        response_code = requests.get(api_url).status_code
        self.assertEqual(response_code, 200)


if __name__ == '__main__':
    unittest.main()
