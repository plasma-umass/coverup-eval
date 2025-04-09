# file: lib/ansible/plugins/filter/core.py:468-486
# asked: {"lines": [468, 470, 471, 472, 474, 475, 476, 477, 478, 480, 482, 484, 486], "branches": [[471, 472], [471, 486], [472, 474], [472, 475], [475, 476], [475, 484], [476, 477], [476, 478], [478, 480], [478, 482]]}
# gained: {"lines": [468, 470, 471, 472, 474, 475, 476, 477, 478, 480, 482, 484, 486], "branches": [[471, 472], [471, 486], [472, 474], [472, 475], [475, 476], [475, 484], [476, 477], [476, 478], [478, 480], [478, 482]]}

import pytest
from ansible.plugins.filter.core import flatten
from ansible.module_utils.common.collections import is_sequence

def test_flatten_with_none_levels():
    assert flatten([1, [2, [3, 4], 5], 6]) == [1, 2, 3, 4, 5, 6]

def test_flatten_with_specific_levels():
    assert flatten([1, [2, [3, 4], 5], 6], levels=1) == [1, 2, [3, 4], 5, 6]

def test_flatten_with_skip_nulls():
    assert flatten([1, None, 'None', 'null', 2, [3, None, 4], 5], skip_nulls=True) == [1, 2, 3, 4, 5]

def test_flatten_without_skip_nulls():
    assert flatten([1, None, 'None', 'null', 2, [3, None, 4], 5], skip_nulls=False) == [1, None, 'None', 'null', 2, 3, None, 4, 5]

def test_flatten_with_empty_list():
    assert flatten([]) == []

def test_flatten_with_non_sequence_elements():
    assert flatten([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_is_sequence_with_list():
    assert is_sequence([1, 2, 3]) == True

def test_is_sequence_with_string():
    assert is_sequence("string") == False

def test_is_sequence_with_string_included():
    assert is_sequence("string", include_strings=True) == True

def test_is_sequence_with_non_sequence():
    assert is_sequence(123) == False
