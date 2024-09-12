# file: lib/ansible/plugins/filter/core.py:468-486
# asked: {"lines": [468, 470, 471, 472, 474, 475, 476, 477, 478, 480, 482, 484, 486], "branches": [[471, 472], [471, 486], [472, 474], [472, 475], [475, 476], [475, 484], [476, 477], [476, 478], [478, 480], [478, 482]]}
# gained: {"lines": [468, 470, 471, 472, 474, 475, 476, 477, 478, 480, 482, 484, 486], "branches": [[471, 472], [471, 486], [472, 474], [472, 475], [475, 476], [475, 484], [476, 477], [476, 478], [478, 480], [478, 482]]}

import pytest
from ansible.plugins.filter.core import flatten
from ansible.module_utils.common.collections import is_sequence

def test_flatten_simple_list():
    assert flatten([1, 2, 3]) == [1, 2, 3]

def test_flatten_nested_list():
    assert flatten([1, [2, 3], 4]) == [1, 2, 3, 4]

def test_flatten_with_levels():
    assert flatten([1, [2, [3, 4]], 5], levels=1) == [1, 2, [3, 4], 5]

def test_flatten_with_skip_nulls():
    assert flatten([1, None, 'None', 'null', 2, [3, None]], skip_nulls=True) == [1, 2, 3]

def test_flatten_without_skip_nulls():
    assert flatten([1, None, 'None', 'null', 2, [3, None]], skip_nulls=False) == [1, None, 'None', 'null', 2, 3, None]

def test_flatten_with_levels_zero():
    assert flatten([1, [2, [3, 4]], 5], levels=0) == [1, [2, [3, 4]], 5]

def test_flatten_empty_list():
    assert flatten([]) == []

def test_flatten_non_sequence_elements():
    assert flatten([1, 'a', [2, 'b'], 3]) == [1, 'a', 2, 'b', 3]

@pytest.fixture(autouse=True)
def mock_is_sequence(monkeypatch):
    def mock_is_sequence(obj):
        return isinstance(obj, (list, tuple))
    monkeypatch.setattr('ansible.module_utils.common.collections.is_sequence', mock_is_sequence)
