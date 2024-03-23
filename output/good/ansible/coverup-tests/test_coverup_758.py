# file lib/ansible/utils/helpers.py:46-51
# lines [46, 50, 51]
# branches []

import pytest

from ansible.utils.helpers import deduplicate_list

def test_deduplicate_list():
    # Test with a list containing duplicates
    original_list = [1, 2, 2, 3, 1, 4, 4, 5]
    expected_result = [1, 2, 3, 4, 5]
    assert deduplicate_list(original_list) == expected_result

    # Test with a list with no duplicates
    original_list_no_duplicates = [1, 2, 3, 4, 5]
    assert deduplicate_list(original_list_no_duplicates) == original_list_no_duplicates

    # Test with an empty list
    empty_list = []
    assert deduplicate_list(empty_list) == empty_list

    # Test with a list of different types
    mixed_list = [1, '1', 2, '2', 1, '1']
    expected_mixed_result = [1, '1', 2, '2']
    assert deduplicate_list(mixed_list) == expected_mixed_result

    # Test with a list of only duplicates
    all_duplicates = [1, 1, 1, 1]
    expected_all_duplicates_result = [1]
    assert deduplicate_list(all_duplicates) == expected_all_duplicates_result
