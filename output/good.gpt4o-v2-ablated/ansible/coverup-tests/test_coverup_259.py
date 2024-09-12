# file: lib/ansible/plugins/callback/minimal.py:76-78
# asked: {"lines": [76, 77, 78], "branches": [[77, 0], [77, 78]]}
# gained: {"lines": [76, 77, 78], "branches": [[77, 0], [77, 78]]}

import pytest
from ansible.plugins.callback.minimal import CallbackModule
from ansible.plugins.callback import CallbackBase
from unittest.mock import Mock

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_on_file_diff_with_diff(callback_module, mocker):
    mock_display = mocker.patch.object(callback_module, '_display')
    mock_get_diff = mocker.patch.object(callback_module, '_get_diff', return_value='mocked_diff')
    
    result = Mock()
    result._result = {'diff': 'some_diff'}
    
    callback_module.v2_on_file_diff(result)
    
    mock_get_diff.assert_called_once_with('some_diff')
    mock_display.display.assert_called_once_with('mocked_diff')

def test_v2_on_file_diff_without_diff(callback_module, mocker):
    mock_display = mocker.patch.object(callback_module, '_display')
    mock_get_diff = mocker.patch.object(callback_module, '_get_diff')
    
    result = Mock()
    result._result = {}
    
    callback_module.v2_on_file_diff(result)
    
    mock_get_diff.assert_not_called()
    mock_display.display.assert_not_called()
