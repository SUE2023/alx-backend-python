#!/usr/bin/env python3
"""Module to test files functions"""

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap class to test the access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test that access_nested_map returns the expected result."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """Test that access_nested_map raises a KeyError for the input"""
        # with self.assertRaises(KeyError) as context:
        #   access_nested_map(nested_map, path)
        # self.assertEqual(str(context.exception), expected)
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
        self.assertEqual(f"KeyError('{expected}')", repr(e.exception))


class TestGetJson(unittest.TestCase):
    """TestGetJson class to test the utils.get_json function. """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """Test that get_json returns expected result and mocks requests.get"""
        with patch('requests.get') as mock_get:
            # Configures mock to return response with the desired JSON payload
            mock_get.return_value.json.return_value = test_payload

            # Call the function and check the result
            result = get_json(test_url)
            self.assertEqual(result, test_payload)

            # Ensure get method was called exactly once with the correct URL
            mock_get.assert_called_once_with(test_url)


if __name__ == "__main__":
    unittest.main()
