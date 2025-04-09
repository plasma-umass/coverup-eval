# file: lib/ansible/plugins/filter/core.py:468-486
# asked: {"lines": [468, 470, 471, 472, 474, 475, 476, 477, 478, 480, 482, 484, 486], "branches": [[471, 472], [471, 486], [472, 474], [472, 475], [475, 476], [475, 484], [476, 477], [476, 478], [478, 480], [478, 482]]}
# gained: {"lines": [468, 470, 471, 472, 474, 475, 476, 477, 478, 480, 482, 484, 486], "branches": [[471, 472], [471, 486], [472, 474], [472, 475], [475, 476], [475, 484], [476, 477], [476, 478], [478, 480], [478, 482]]}

import pytest
from ansible.plugins.filter.core import flatten
from ansible.module_utils.common.collections import is_sequence

def test_flatten_with_none_levels():
    mylist = [1, [2, [3, None]], 'None', 'null']
    result = flatten(mylist)
    assert result == [1, 2, 3]

def test_flatten_with_specific_levels():
    mylist = [1, [2, [3, 4]], 5]
    result = flatten(mylist, levels=1)
    assert result == [1, 2, [3, 4], 5]

def test_flatten_with_skip_nulls_false():
    mylist = [1, [2, [3, None]], 'None', 'null']
    result = flatten(mylist, skip_nulls=False)
    assert result == [1, 2, 3, None, 'None', 'null']

def test_flatten_with_non_sequence():
    mylist = [1, 2, 3]
    result = flatten(mylist)
    assert result == [1, 2, 3]

def test_flatten_with_empty_list():
    mylist = []
    result = flatten(mylist)
    assert result == []

def test_flatten_with_nested_empty_list():
    mylist = [1, [], [2, []], 3]
    result = flatten(mylist)
    assert result == [1, 2, 3]
