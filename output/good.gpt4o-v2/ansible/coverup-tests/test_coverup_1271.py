# file: lib/ansible/inventory/manager.py:500-531
# asked: {"lines": [526], "branches": [[525, 526]]}
# gained: {"lines": [526], "branches": [[525, 526]]}

import pytest
from ansible.inventory.manager import InventoryManager
import re
from ansible.utils.display import Display

PATTERN_WITH_SUBSCRIPT = re.compile(r'''
    ^
    (.+)                    # A pattern expression ending with...
    \[(?:                   # A [subscript] expression comprising:
        (-?[0-9]+)|         # A single positive or negative number
        ([0-9]+)([:-])      # Or an x:y or x: range.
        ([0-9]*)
    )\]
    $
''', re.X)

@pytest.fixture
def inventory_manager():
    return InventoryManager(loader=None)

def test_split_subscript_no_subscript(inventory_manager):
    pattern = "host_pattern"
    result = inventory_manager._split_subscript(pattern)
    assert result == (pattern, None)

def test_split_subscript_with_tilde(inventory_manager):
    pattern = "~host_pattern"
    result = inventory_manager._split_subscript(pattern)
    assert result == (pattern, None)

def test_split_subscript_with_single_index(inventory_manager):
    pattern = "host_pattern[5]"
    result = inventory_manager._split_subscript(pattern)
    assert result == ("host_pattern", (5, None))

def test_split_subscript_with_range(inventory_manager):
    pattern = "host_pattern[1:5]"
    result = inventory_manager._split_subscript(pattern)
    assert result == ("host_pattern", (1, 5))

def test_split_subscript_with_range_no_end(inventory_manager):
    pattern = "host_pattern[1:]"
    result = inventory_manager._split_subscript(pattern)
    assert result == ("host_pattern", (1, -1))

def test_split_subscript_with_negative_index(inventory_manager):
    pattern = "host_pattern[-1]"
    result = inventory_manager._split_subscript(pattern)
    assert result == ("host_pattern", (-1, None))

def test_split_subscript_with_warning(mocker, inventory_manager):
    pattern = "host_pattern[1-5]"
    mocker.patch.object(Display, 'warning')
    result = inventory_manager._split_subscript(pattern)
    assert result == ("host_pattern", (1, 5))
