# file: lib/ansible/utils/helpers.py:46-51
# asked: {"lines": [46, 50, 51], "branches": []}
# gained: {"lines": [46, 50, 51], "branches": []}

import pytest

from ansible.utils.helpers import deduplicate_list

def test_deduplicate_list_empty():
    assert deduplicate_list([]) == []

def test_deduplicate_list_no_duplicates():
    assert deduplicate_list([1, 2, 3]) == [1, 2, 3]

def test_deduplicate_list_with_duplicates():
    assert deduplicate_list([1, 2, 2, 3, 1]) == [1, 2, 3]

def test_deduplicate_list_all_duplicates():
    assert deduplicate_list([1, 1, 1, 1]) == [1]

def test_deduplicate_list_strings():
    assert deduplicate_list(['a', 'b', 'a', 'c', 'b']) == ['a', 'b', 'c']

def test_deduplicate_list_mixed_types():
    assert deduplicate_list([1, 'a', 1, 'b', 'a']) == [1, 'a', 'b']
