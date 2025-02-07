# file: lib/ansible/inventory/group.py:32-53
# asked: {"lines": [39, 40, 41, 42, 43, 44, 46, 47, 48, 51], "branches": [[38, 39], [40, 41], [40, 46], [42, 43], [42, 50], [46, 47], [46, 50], [50, 51]]}
# gained: {"lines": [39, 40, 41, 42, 43, 44, 46, 47, 48, 51], "branches": [[38, 39], [40, 41], [40, 46], [42, 43], [42, 50], [46, 47], [50, 51]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.inventory.group import to_safe_group_name
from ansible import constants as C

@pytest.fixture
def mock_display():
    with patch('ansible.inventory.group.display') as mock_display:
        yield mock_display

def test_to_safe_group_name_invalid_chars_replaced(mock_display):
    C.TRANSFORM_INVALID_GROUP_CHARS = 'something'
    name = "invalid!name"
    result = to_safe_group_name(name)
    assert result == "invalid_name"
    mock_display.vvvv.assert_called_once_with('Replacing invalid character(s) "{\'!\'}" in group name (invalid!name)')
    mock_display.warning.assert_called_once_with('Invalid characters were found in group names and automatically replaced, use -vvvv to see details')

def test_to_safe_group_name_invalid_chars_not_replaced(mock_display):
    C.TRANSFORM_INVALID_GROUP_CHARS = 'never'
    name = "invalid!name"
    result = to_safe_group_name(name)
    assert result == "invalid!name"
    mock_display.vvvv.assert_called_once_with('Not replacing invalid character(s) "{\'!\'}" in group name (invalid!name)')
    mock_display.warning.assert_called_once_with('Invalid characters were found in group names but not replaced, use -vvvv to see details')

def test_to_safe_group_name_invalid_chars_force_replace(mock_display):
    C.TRANSFORM_INVALID_GROUP_CHARS = 'never'
    name = "invalid!name"
    result = to_safe_group_name(name, force=True)
    assert result == "invalid_name"
    mock_display.vvvv.assert_called_once_with('Replacing invalid character(s) "{\'!\'}" in group name (invalid!name)')
    mock_display.warning.assert_called_once_with('Invalid characters were found in group names and automatically replaced, use -vvvv to see details')

def test_to_safe_group_name_invalid_chars_silent(mock_display):
    C.TRANSFORM_INVALID_GROUP_CHARS = 'something'
    name = "invalid!name"
    result = to_safe_group_name(name, silent=True)
    assert result == "invalid_name"
    mock_display.vvvv.assert_not_called()
    mock_display.warning.assert_not_called()
