# file: lib/ansible/plugins/filter/core.py:468-486
# asked: {"lines": [468, 470, 471, 472, 474, 475, 476, 477, 478, 480, 482, 484, 486], "branches": [[471, 472], [471, 486], [472, 474], [472, 475], [475, 476], [475, 484], [476, 477], [476, 478], [478, 480], [478, 482]]}
# gained: {"lines": [468, 470, 471, 472, 474, 475, 476, 477, 478, 480, 482, 484, 486], "branches": [[471, 472], [471, 486], [472, 474], [472, 475], [475, 476], [475, 484], [476, 477], [476, 478], [478, 480], [478, 482]]}

import pytest
from ansible.plugins.filter.core import flatten

def test_flatten_skip_nulls_true():
    assert flatten([1, 2, None, 3, 'None', 'null', 4]) == [1, 2, 3, 4]

def test_flatten_skip_nulls_false():
    assert flatten([1, 2, None, 3, 'None', 'null', 4], skip_nulls=False) == [1, 2, None, 3, 'None', 'null', 4]

def test_flatten_with_levels():
    assert flatten([1, [2, [3, [4]]]], levels=1) == [1, 2, [3, [4]]]
    assert flatten([1, [2, [3, [4]]]], levels=2) == [1, 2, 3, [4]]
    assert flatten([1, [2, [3, [4]]]], levels=3) == [1, 2, 3, 4]

def test_flatten_no_levels():
    assert flatten([1, [2, [3, [4]]]]) == [1, 2, 3, 4]

def test_flatten_empty_list():
    assert flatten([]) == []

def test_flatten_non_sequence_elements():
    assert flatten([1, 'a', [2, 'b', [3, 'c']]]) == [1, 'a', 2, 'b', 3, 'c']

@pytest.fixture(autouse=True)
def run_around_tests():
    # Setup: nothing to setup
    yield
    # Teardown: nothing to teardown
