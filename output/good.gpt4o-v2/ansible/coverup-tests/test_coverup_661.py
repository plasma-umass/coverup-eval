# file: lib/ansible/plugins/callback/minimal.py:76-78
# asked: {"lines": [76, 77, 78], "branches": [[77, 0], [77, 78]]}
# gained: {"lines": [76, 77, 78], "branches": [[77, 0], [77, 78]]}

import pytest
from unittest.mock import Mock, MagicMock
from ansible.plugins.callback.minimal import CallbackModule

@pytest.fixture
def callback_module():
    display = MagicMock()
    display.verbosity = 0
    return CallbackModule(display=display)

def test_v2_on_file_diff_with_diff(callback_module):
    result = Mock()
    result._result = {'diff': 'some_diff'}
    
    callback_module.v2_on_file_diff(result)
    
    callback_module._display.display.assert_called_once_with(callback_module._get_diff('some_diff'))

def test_v2_on_file_diff_without_diff(callback_module):
    result = Mock()
    result._result = {}
    
    callback_module.v2_on_file_diff(result)
    
    callback_module._display.display.assert_not_called()
