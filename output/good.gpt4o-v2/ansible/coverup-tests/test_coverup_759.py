# file: lib/ansible/utils/helpers.py:46-51
# asked: {"lines": [46, 50, 51], "branches": []}
# gained: {"lines": [46, 50, 51], "branches": []}

import pytest
from ansible.utils.helpers import deduplicate_list

def test_deduplicate_list():
    # Test with a list containing duplicates
    original_list = [1, 2, 2, 3, 4, 4, 5]
    expected_result = [1, 2, 3, 4, 5]
    assert deduplicate_list(original_list) == expected_result

    # Test with a list without duplicates
    original_list = [1, 2, 3, 4, 5]
    expected_result = [1, 2, 3, 4, 5]
    assert deduplicate_list(original_list) == expected_result

    # Test with an empty list
    original_list = []
    expected_result = []
    assert deduplicate_list(original_list) == expected_result

    # Test with a list of strings
    original_list = ["a", "b", "a", "c", "b"]
    expected_result = ["a", "b", "c"]
    assert deduplicate_list(original_list) == expected_result

    # Test with a list of mixed types
    original_list = [1, "a", 1, "b", "a"]
    expected_result = [1, "a", "b"]
    assert deduplicate_list(original_list) == expected_result
