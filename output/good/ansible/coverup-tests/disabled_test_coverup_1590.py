# file lib/ansible/inventory/manager.py:500-531
# lines [512, 525, 526, 527, 528, 529]
# branches ['511->512', '522->525', '525->526', '525->527', '528->529', '528->531']

import pytest
from ansible.inventory.manager import InventoryManager
from ansible.utils.display import Display
from unittest.mock import MagicMock

# Mock the Display class to capture warnings
@pytest.fixture
def mock_display(mocker):
    mocker.patch('ansible.utils.display.Display.warning')

# Mock the DataLoader class
@pytest.fixture
def mock_loader(mocker):
    return MagicMock()

# Test function to cover missing lines
def test_split_subscript_with_tilde_and_range(mock_display, mock_loader):
    inventory_manager = InventoryManager(loader=mock_loader)

    # Test with a pattern starting with tilde
    pattern_with_tilde = "~some_pattern"
    result = inventory_manager._split_subscript(pattern_with_tilde)
    assert result == (pattern_with_tilde, None), "Pattern starting with tilde should return itself and None"

    # Test with a pattern containing a range with a hyphen
    pattern_with_range_hyphen = "some_pattern[1-2]"
    result = inventory_manager._split_subscript(pattern_with_range_hyphen)
    assert result == ("some_pattern", (1, 2)), "Pattern with range should return the pattern and the range tuple"
    Display.warning.assert_any_call("Use [x:y] inclusive subscripts instead of [x-y] which has been removed")

    # Test with a pattern containing a range without an end
    pattern_with_range_no_end = "some_pattern[1:]"
    result = inventory_manager._split_subscript(pattern_with_range_no_end)
    assert result == ("some_pattern", (1, -1)), "Pattern with range without an end should return the pattern and the range tuple with -1 as end"

    # Clean up after the test
    Display.warning.reset_mock()
