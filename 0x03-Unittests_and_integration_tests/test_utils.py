#!/usr/bin/env python3
""" 
    Parameterize a unit test
"""
import unittest
import requests
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize
from typing import Mapping, Sequence, Any
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """ 
        first unit test for utils.access_nested_map
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected: int) -> None:
        """
            This Tests access_nested_map method.
            Nested_map(Dict): dictonary
            path(List, tuple, set): keys to get value in nested dect
        """
        response = access_nested_map(nested_map, path)
        self.assertEqual(response, expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence) -> None:
        """
            Test access nested map exception
            Args:
                nested_map (Dict): A Dictonary
                path(List, Tuple, set): key to get value of nested dect
        """
        with self.assertRaises(Exception):
            access_nested_map(nested_map, path)
            