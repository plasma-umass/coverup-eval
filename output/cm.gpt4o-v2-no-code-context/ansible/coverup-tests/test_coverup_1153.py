# file: lib/ansible/inventory/group.py:32-53
# asked: {"lines": [39, 40, 41, 42, 43, 44, 46, 47, 48, 51], "branches": [[38, 39], [40, 41], [40, 46], [42, 43], [42, 50], [46, 47], [46, 50], [50, 51]]}
# gained: {"lines": [39, 40, 41, 42, 43, 44, 46, 47, 48, 51], "branches": [[38, 39], [40, 41], [40, 46], [42, 43], [46, 47], [46, 50], [50, 51]]}

import pytest
from unittest.mock import patch, MagicMock

# Mocking the necessary parts
@pytest.fixture
def mock_constants(monkeypatch):
    class MockConstants:
        INVALID_VARIABLE_NAMES = MagicMock()
        TRANSFORM_INVALID_GROUP_CHARS = 'never'
    
    constants = MockConstants()
    monkeypatch.setattr('ansible.inventory.group.C', constants)
    return constants

@pytest.fixture
def mock_display(monkeypatch):
    display = MagicMock()
    monkeypatch.setattr('ansible.inventory.group.display', display)
    return display

def test_to_safe_group_name_invalid_chars_force(mock_constants, mock_display):
    from ansible.inventory.group import to_safe_group_name

    mock_constants.INVALID_VARIABLE_NAMES.findall.return_value = ['!']
    mock_constants.INVALID_VARIABLE_NAMES.sub.return_value = 'group_name'
    mock_constants.TRANSFORM_INVALID_GROUP_CHARS = 'never'

    result = to_safe_group_name('group!name', force=True)

    assert result == 'group_name'
    mock_display.vvvv.assert_called_once_with('Replacing invalid character(s) "{\'!\'}" in group name (group!name)')
    mock_display.warning.assert_called_once_with('Invalid characters were found in group names and automatically replaced, use -vvvv to see details')

def test_to_safe_group_name_invalid_chars_never(mock_constants, mock_display):
    from ansible.inventory.group import to_safe_group_name

    mock_constants.INVALID_VARIABLE_NAMES.findall.return_value = ['!']
    mock_constants.TRANSFORM_INVALID_GROUP_CHARS = 'never'

    result = to_safe_group_name('group!name')

    assert result == 'group!name'
    mock_display.vvvv.assert_called_once_with('Not replacing invalid character(s) "{\'!\'}" in group name (group!name)')
    mock_display.warning.assert_called_once_with('Invalid characters were found in group names but not replaced, use -vvvv to see details')

def test_to_safe_group_name_invalid_chars_ignore(mock_constants, mock_display):
    from ansible.inventory.group import to_safe_group_name

    mock_constants.INVALID_VARIABLE_NAMES.findall.return_value = ['!']
    mock_constants.TRANSFORM_INVALID_GROUP_CHARS = 'ignore'

    result = to_safe_group_name('group!name')

    assert result == 'group!name'
    mock_display.vvvv.assert_not_called()
    mock_display.warning.assert_not_called()
