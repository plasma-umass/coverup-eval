# file: lib/ansible/inventory/manager.py:500-531
# asked: {"lines": [500, 511, 512, 518, 519, 520, 521, 522, 523, 525, 526, 527, 528, 529, 531], "branches": [[511, 512], [511, 518], [520, 521], [520, 531], [522, 523], [522, 525], [525, 526], [525, 527], [528, 529], [528, 531]]}
# gained: {"lines": [500, 511, 512, 518, 519, 520, 521, 522, 523, 525, 526, 527, 528, 529, 531], "branches": [[511, 512], [511, 518], [520, 521], [520, 531], [522, 523], [522, 525], [525, 526], [525, 527], [528, 529], [528, 531]]}

import pytest
from ansible.inventory.manager import InventoryManager
import re

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

def test_split_subscript_regex(inventory_manager):
    pattern = "~regex_pattern"
    result = inventory_manager._split_subscript(pattern)
    assert result == (pattern, None)

def test_split_subscript_single_index(inventory_manager):
    pattern = "host_pattern[5]"
    result = inventory_manager._split_subscript(pattern)
    assert result == ("host_pattern", (5, None))

def test_split_subscript_range(inventory_manager):
    pattern = "host_pattern[1:5]"
    result = inventory_manager._split_subscript(pattern)
    assert result == ("host_pattern", (1, 5))

def test_split_subscript_range_with_dash(inventory_manager, mocker):
    pattern = "host_pattern[1-5]"
    mock_warning = mocker.patch('ansible.utils.display.Display.warning')
    result = inventory_manager._split_subscript(pattern)
    assert result == ("host_pattern", (1, 5))
    mock_warning.assert_called_once_with("Use [x:y] inclusive subscripts instead of [x-y] which has been removed")

def test_split_subscript_range_no_end(inventory_manager):
    pattern = "host_pattern[1:]"
    result = inventory_manager._split_subscript(pattern)
    assert result == ("host_pattern", (1, -1))
