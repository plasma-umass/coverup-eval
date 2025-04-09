# file lib/ansible/utils/helpers.py:46-51
# lines [46, 50, 51]
# branches []

import pytest
from ansible.utils.helpers import deduplicate_list

def test_deduplicate_list():
    # Test with a list containing duplicates
    original_list = [1, 2, 2, 3, 4, 4, 5]
    deduplicated = deduplicate_list(original_list)
    assert deduplicated == [1, 2, 3, 4, 5]

    # Test with a list with no duplicates
    original_list = [1, 2, 3, 4, 5]
    deduplicated = deduplicate_list(original_list)
    assert deduplicated == [1, 2, 3, 4, 5]

    # Test with an empty list
    original_list = []
    deduplicated = deduplicate_list(original_list)
    assert deduplicated == []

    # Test with a list of strings
    original_list = ["a", "b", "a", "c", "b"]
    deduplicated = deduplicate_list(original_list)
    assert deduplicated == ["a", "b", "c"]

    # Test with a list of mixed types
    original_list = [1, "a", 1, "b", "a"]
    deduplicated = deduplicate_list(original_list)
    assert deduplicated == [1, "a", "b"]
