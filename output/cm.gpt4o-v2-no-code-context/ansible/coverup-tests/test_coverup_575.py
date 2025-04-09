# file: lib/ansible/plugins/callback/minimal.py:76-78
# asked: {"lines": [76, 77, 78], "branches": [[77, 0], [77, 78]]}
# gained: {"lines": [76, 77, 78], "branches": [[77, 0], [77, 78]]}

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.callback.minimal import CallbackModule

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_on_file_diff_executes(callback_module, mocker):
    # Mocking the result object
    result = Mock()
    result._result = {'diff': 'some_diff'}

    # Mocking the _display and _get_diff methods
    mock_display = mocker.patch.object(callback_module, '_display')
    mock_get_diff = mocker.patch.object(callback_module, '_get_diff', return_value='formatted_diff')

    # Call the method
    callback_module.v2_on_file_diff(result)

    # Assertions to ensure the lines are executed
    mock_get_diff.assert_called_once_with('some_diff')
    mock_display.display.assert_called_once_with('formatted_diff')

def test_v2_on_file_diff_no_diff(callback_module, mocker):
    # Mocking the result object with no 'diff' key
    result = Mock()
    result._result = {}

    # Mocking the _display and _get_diff methods
    mock_display = mocker.patch.object(callback_module, '_display')
    mock_get_diff = mocker.patch.object(callback_module, '_get_diff')

    # Call the method
    callback_module.v2_on_file_diff(result)

    # Assertions to ensure the lines are not executed
    mock_get_diff.assert_not_called()
    mock_display.display.assert_not_called()

def test_v2_on_file_diff_empty_diff(callback_module, mocker):
    # Mocking the result object with an empty 'diff'
    result = Mock()
    result._result = {'diff': ''}

    # Mocking the _display and _get_diff methods
    mock_display = mocker.patch.object(callback_module, '_display')
    mock_get_diff = mocker.patch.object(callback_module, '_get_diff')

    # Call the method
    callback_module.v2_on_file_diff(result)

    # Assertions to ensure the lines are not executed
    mock_get_diff.assert_not_called()
    mock_display.display.assert_not_called()
