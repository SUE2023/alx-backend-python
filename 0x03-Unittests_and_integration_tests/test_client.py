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

    @patch('client.GithubOrgClient.org', new_callable=unittest.mock.\\n
           PropertyMock)
    def test_public_repos_url(self, mock_org):
        """Unit-test GithubOrgClient._public_repos_url"""
        test_payload = {"repos_url": "https://api.github.\
                        com/orgs/google/repos"}
        mock_org.return_value = test_payload

        client = GithubOrgClient("google")
        result = client._public_repos_url
        self.assertEqual(result, test_payload["repos_url"])
        mock_org.assert_called_once()


if __name__ == "__main__":
    unittest.main()
