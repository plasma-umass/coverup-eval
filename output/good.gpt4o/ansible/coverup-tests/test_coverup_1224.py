# file lib/ansible/plugins/callback/minimal.py:76-78
# lines [77, 78]
# branches ['77->exit', '77->78']

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.callback.minimal import CallbackModule

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_on_file_diff_executes_lines_77_78(callback_module, mocker):
    mock_display = mocker.patch.object(callback_module, '_display')
    mock_get_diff = mocker.patch.object(callback_module, '_get_diff', return_value='mocked_diff_output')
    
    result = Mock()
    result._result = {'diff': 'some_diff_data'}
    
    callback_module.v2_on_file_diff(result)
    
    mock_get_diff.assert_called_once_with('some_diff_data')
    mock_display.display.assert_called_once_with('mocked_diff_output')
