#!/usr/bin/env python3
"""Module for testing GithubOrgClient."""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient
from utils import get_json


class TestGithubOrgClient(unittest.TestCase):
    """Class to test the GithubOrgClient class."""

    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"})
    ])
    @patch('client.get_json', return_value={"login": "google"})
    def test_org(self, org_name, expected_response, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value."""
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org(), expected_response)
        mock_get_json.assert_called_once_with(f"https://api.github.\
                                              com/orgs/{org_name}")


if __name__ == "__main__":
    unittest.main()
