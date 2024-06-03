# file lib/ansible/inventory/group.py:32-53
# lines []
# branches ['42->50', '46->50']

import pytest
from unittest import mock
from ansible.inventory.group import to_safe_group_name

@pytest.fixture
def mock_display(mocker):
    return mocker.patch('ansible.inventory.group.display')

@pytest.fixture
def mock_config(mocker):
    mock_C = mocker.patch('ansible.inventory.group.C')
    mock_C.INVALID_VARIABLE_NAMES = mock.Mock()
    mock_C.TRANSFORM_INVALID_GROUP_CHARS = 'never'
    return mock_C

def test_to_safe_group_name_never_replace(mock_display, mock_config):
    mock_config.INVALID_VARIABLE_NAMES.findall.return_value = ['!']
    mock_config.INVALID_VARIABLE_NAMES.sub.return_value = 'group_name'
    
    result = to_safe_group_name('group!name', silent=False)
    
    assert result == 'group!name'
    mock_display.vvvv.assert_called_once_with('Not replacing invalid character(s) "{\'!\'}" in group name (group!name)')
    mock_display.warning.assert_called_once_with('Invalid characters were found in group names but not replaced, use -vvvv to see details')

def test_to_safe_group_name_silent(mock_display, mock_config):
    mock_config.INVALID_VARIABLE_NAMES.findall.return_value = ['!']
    mock_config.INVALID_VARIABLE_NAMES.sub.return_value = 'group_name'
    mock_config.TRANSFORM_INVALID_GROUP_CHARS = 'silently'
    
    result = to_safe_group_name('group!name', silent=True)
    
    assert result == 'group_name'
    mock_display.vvvv.assert_not_called()
    mock_display.warning.assert_not_called()
