#!/usr/bin/env python3
"""Module for testing GithubOrgClient."""

import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from utils import get_json
from fixtures import TEST_PAYLOAD


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

    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        """
        Test that the list of repos is what is expect from the chosen payload.
        Test that the mocked property and the mocked get_json was called once.
        """
        json_payload = [{"name": "Google"}, {"name": "Linkedin"}]
        mock_json.return_value = json_payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public:

            mock_public.return_value = "hello/world"
            test_class = GithubOrgClient('test')
            result = test_class.public_repos()

            check = [i["name"] for i in json_payload]
            self.assertEqual(result, check)

            mock_public.assert_called_once()
            mock_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ({}, "my_license", False),  # Edge case: no license in repo
        ({"license": {}}, "my_license", False),  # Edge case: empty dict
    ])
    def test_has_license(self, repo, license_key, expected):
        """Unit-test for GithubOrgClient.has_license"""
        client = GithubOrgClient("test_org")  # Use a dummy org name
        result = client.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class([
    {"org_payload": org_payload, "repos_payload": repos_payload,
     "expected_repos": expected_repos, "apache2_repos": apache2_repos}
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test class to test GithubOrgClient using fixtures."""

    @classmethod
    def setUpClass(cls):
        """Class method called before tests in the class are run."""
        # Patch requests.get, configure it to return the appropriate payloads
        config = {'json.side_effect': [cls.org_payload, cls.repos_payload]}
        cls.get_patcher = patch('requests.get', **config)
        cls.mock_get = cls.get_patcher.start()

    def test_public_repos(self):
        """Integration test: public repos."""
        test_class = GithubOrgClient("google")

        self.assertEqual(test_class.org, self.org_payload)
        self.assertEqual(test_class._public_repos_url,
                         self.repos_payload['repos_url'])
        self.assertEqual(test_class.public_repos(), self.expected_repos)
        self.assertEqual(test_class.public_repos("XLICENSE"), [])
        self.mock_get.assert_called()

    def test_public_repos_with_license(self):
        """Integration test for public repos with a specific license."""
        test_class = GithubOrgClient("google")

        self.assertEqual(test_class.public_repos(), self.expected_repos)
        self.assertEqual(test_class.public_repos("XLICENSE"), [])
        self.assertEqual(test_class.public_repos("apache-2.0"),
                         self.apache2_repos)
        self.mock_get.assert_called()

    @classmethod
    def tearDownClass(cls):
        """Class method called after tests in the class have run."""
        cls.get_patcher.stop()


if __name__ == "__main__":
    unittest.main()
