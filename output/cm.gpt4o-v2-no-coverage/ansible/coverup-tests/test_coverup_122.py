# file: lib/ansible/inventory/group.py:32-53
# asked: {"lines": [32, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 47, 48, 50, 51, 53], "branches": [[36, 37], [36, 50], [38, 39], [38, 50], [40, 41], [40, 46], [42, 43], [42, 50], [46, 47], [46, 50], [50, 51], [50, 53]]}
# gained: {"lines": [32, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 47, 48, 50, 51, 53], "branches": [[36, 37], [36, 50], [38, 39], [38, 50], [40, 41], [40, 46], [42, 43], [42, 50], [46, 47], [50, 51], [50, 53]]}

import pytest
from ansible.module_utils._text import to_text
from ansible.inventory.group import to_safe_group_name
from unittest.mock import patch, MagicMock

@pytest.fixture
def mock_display(mocker):
    return mocker.patch('ansible.inventory.group.display')

@pytest.fixture
def mock_constants():
    mock_constants = MagicMock()
    mock_constants.INVALID_VARIABLE_NAMES.findall.return_value = []
    mock_constants.TRANSFORM_INVALID_GROUP_CHARS = 'never'
    return mock_constants

def test_to_safe_group_name_no_name(mock_display, mock_constants):
    with patch('ansible.inventory.group.C', mock_constants):
        assert to_safe_group_name('') == ''
        mock_display.warning.assert_not_called()

def test_to_safe_group_name_no_invalid_chars(mock_display, mock_constants):
    with patch('ansible.inventory.group.C', mock_constants):
        mock_constants.INVALID_VARIABLE_NAMES.findall.return_value = []
        assert to_safe_group_name('valid_name') == 'valid_name'
        mock_display.warning.assert_not_called()

def test_to_safe_group_name_with_invalid_chars_replace(mock_display, mock_constants):
    with patch('ansible.inventory.group.C', mock_constants):
        mock_constants.INVALID_VARIABLE_NAMES.findall.return_value = ['!']
        mock_constants.TRANSFORM_INVALID_GROUP_CHARS = 'replace'
        mock_constants.INVALID_VARIABLE_NAMES.sub.return_value = 'valid_name'
        assert to_safe_group_name('invalid!name') == 'valid_name'
        mock_display.vvvv.assert_called_once_with('Replacing invalid character(s) "{\'!\'}" in group name (invalid!name)')
        mock_display.warning.assert_called_once_with('Invalid characters were found in group names and automatically replaced, use -vvvv to see details')

def test_to_safe_group_name_with_invalid_chars_never(mock_display, mock_constants):
    with patch('ansible.inventory.group.C', mock_constants):
        mock_constants.INVALID_VARIABLE_NAMES.findall.return_value = ['!']
        mock_constants.TRANSFORM_INVALID_GROUP_CHARS = 'never'
        assert to_safe_group_name('invalid!name') == 'invalid!name'
        mock_display.vvvv.assert_called_once_with('Not replacing invalid character(s) "{\'!\'}" in group name (invalid!name)')
        mock_display.warning.assert_called_once_with('Invalid characters were found in group names but not replaced, use -vvvv to see details')

def test_to_safe_group_name_with_invalid_chars_force(mock_display, mock_constants):
    with patch('ansible.inventory.group.C', mock_constants):
        mock_constants.INVALID_VARIABLE_NAMES.findall.return_value = ['!']
        mock_constants.TRANSFORM_INVALID_GROUP_CHARS = 'never'
        mock_constants.INVALID_VARIABLE_NAMES.sub.return_value = 'valid_name'
        assert to_safe_group_name('invalid!name', force=True) == 'valid_name'
        mock_display.vvvv.assert_called_once_with('Replacing invalid character(s) "{\'!\'}" in group name (invalid!name)')
        mock_display.warning.assert_called_once_with('Invalid characters were found in group names and automatically replaced, use -vvvv to see details')

def test_to_safe_group_name_with_invalid_chars_silent(mock_display, mock_constants):
    with patch('ansible.inventory.group.C', mock_constants):
        mock_constants.INVALID_VARIABLE_NAMES.findall.return_value = ['!']
        mock_constants.TRANSFORM_INVALID_GROUP_CHARS = 'replace'
        mock_constants.INVALID_VARIABLE_NAMES.sub.return_value = 'valid_name'
        assert to_safe_group_name('invalid!name', silent=True) == 'valid_name'
        mock_display.vvvv.assert_not_called()
        mock_display.warning.assert_not_called()
