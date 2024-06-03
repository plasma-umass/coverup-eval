# file lib/ansible/inventory/group.py:32-53
# lines [39, 40, 41, 42, 43, 44, 46, 47, 48, 51]
# branches ['38->39', '40->41', '40->46', '42->43', '42->50', '46->47', '46->50', '50->51']

import pytest
from unittest import mock
from ansible.inventory.group import to_safe_group_name

@pytest.fixture
def mock_display(mocker):
    return mocker.patch('ansible.inventory.group.display')

@pytest.fixture
def mock_config(mocker):
    config_mock = mocker.patch('ansible.inventory.group.C', autospec=True)
    config_mock.INVALID_VARIABLE_NAMES = mock.Mock()
    return config_mock

def test_to_safe_group_name_invalid_chars_replaced(mock_display, mock_config):
    mock_config.INVALID_VARIABLE_NAMES.findall.return_value = ['!']
    mock_config.INVALID_VARIABLE_NAMES.sub.return_value = 'valid_name'
    mock_config.TRANSFORM_INVALID_GROUP_CHARS = 'always'

    result = to_safe_group_name('invalid!name', force=True)

    assert result == 'valid_name'
    mock_display.vvvv.assert_called_once_with('Replacing invalid character(s) "{\'!\'}" in group name (invalid!name)')
    mock_display.warning.assert_called_once_with('Invalid characters were found in group names and automatically replaced, use -vvvv to see details')

def test_to_safe_group_name_invalid_chars_not_replaced(mock_display, mock_config):
    mock_config.INVALID_VARIABLE_NAMES.findall.return_value = ['!']
    mock_config.TRANSFORM_INVALID_GROUP_CHARS = 'never'

    result = to_safe_group_name('invalid!name')

    assert result == 'invalid!name'
    mock_display.vvvv.assert_called_once_with('Not replacing invalid character(s) "{\'!\'}" in group name (invalid!name)')
    mock_display.warning.assert_called_once_with('Invalid characters were found in group names but not replaced, use -vvvv to see details')
