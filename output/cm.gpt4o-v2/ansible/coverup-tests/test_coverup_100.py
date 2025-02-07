# file: lib/ansible/inventory/manager.py:500-531
# asked: {"lines": [500, 511, 512, 518, 519, 520, 521, 522, 523, 525, 526, 527, 528, 529, 531], "branches": [[511, 512], [511, 518], [520, 521], [520, 531], [522, 523], [522, 525], [525, 526], [525, 527], [528, 529], [528, 531]]}
# gained: {"lines": [500, 511, 512, 518, 519, 520, 521, 522, 523, 525, 527, 528, 529, 531], "branches": [[511, 512], [511, 518], [520, 521], [520, 531], [522, 523], [522, 525], [525, 527], [528, 529], [528, 531]]}

import pytest
from ansible.inventory.manager import InventoryManager
import re
from ansible.utils.display import Display

# Mocking the PATTERN_WITH_SUBSCRIPT as it is a regex pattern
PATTERN_WITH_SUBSCRIPT = re.compile(r'''
    ^                   # Beginning of string
    (.+)                # A pattern expression ending with...
    \[(?:               # A [subscript] expression comprising:
        (-?[0-9]+)|     # A single positive or negative number
        ([0-9]+)([:-])  # Or an x:y or x: range.
        ([0-9]*)        # Optional end of range
    )\]                 # Closing bracket
    $                   # End of string
''', re.X)

@pytest.fixture
def inventory_manager():
    return InventoryManager(loader=None)

def test_split_subscript_no_subscript(inventory_manager):
    pattern = "host_pattern"
    result = inventory_manager._split_subscript(pattern)
    assert result == (pattern, None)

def test_split_subscript_tilde(inventory_manager):
    pattern = "~host_pattern"
    result = inventory_manager._split_subscript(pattern)
    assert result == (pattern, None)

def test_split_subscript_single_index(inventory_manager):
    pattern = "host_pattern[5]"
    result = inventory_manager._split_subscript(pattern)
    assert result == ("host_pattern", (5, None))

def test_split_subscript_range(inventory_manager, mocker):
    pattern = "host_pattern[1:10]"
    mocker.patch.object(Display, 'warning')
    result = inventory_manager._split_subscript(pattern)
    assert result == ("host_pattern", (1, 10))
    assert not Display.warning.called

def test_split_subscript_negative_index(inventory_manager):
    pattern = "host_pattern[-1]"
    result = inventory_manager._split_subscript(pattern)
    assert result == ("host_pattern", (-1, None))

def test_split_subscript_range_with_dash(inventory_manager, mocker):
    pattern = "host_pattern[1-10]"
    mock_warning = mocker.patch.object(Display, 'warning')
    result = inventory_manager._split_subscript(pattern)
    assert result == ("host_pattern", (1, 10))
    mock_warning.assert_called_once_with("Use [x:y] inclusive subscripts instead of [x-y] which has been removed")
