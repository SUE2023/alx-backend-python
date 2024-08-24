#!/usr/bin/env python3
"""Module to test files functions"""

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
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


class TestMemoize(unittest.TestCase):
    """ Class to rest memoization function"""
    def test_memoize():
        """ Test that on calling a_property twice, the correct result is
        returned but a_method is only called once by assert_called_once.
        """

        class TestClass:

            def a_method(self):
                return 42

        @memoize
        def a_property(self):
            return self.a_method()

        # with patch.object(TestClass, 'a_method') as mock:
        #  test_class = TestClass()
        #  test_class.a_property()
        #  test_class.a_property()
        #  mock.assert_called_once()
        with patch.object(TestClass, 'a_method', return_value=42) \
                as mock_method:
            test_class = TestClass()
            self.assertEqual(test_class.a_property, 42)
            # First call, should invoke a_method
            self.assertEqual(test_class.a_property, 42)
            # Second call, should not invoke a_method
            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
