# file: lib/ansible/plugins/callback/minimal.py:76-78
# asked: {"lines": [77, 78], "branches": [[77, 0], [77, 78]]}
# gained: {"lines": [77, 78], "branches": [[77, 0], [77, 78]]}

import pytest
from unittest.mock import Mock
from ansible.plugins.callback.minimal import CallbackModule

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_on_file_diff_with_diff(callback_module):
    result = Mock()
    result._result = {'diff': 'some_diff'}
    callback_module._display = Mock()
    callback_module._get_diff = Mock(return_value='formatted_diff')

    callback_module.v2_on_file_diff(result)

    callback_module._display.display.assert_called_once_with('formatted_diff')
    callback_module._get_diff.assert_called_once_with('some_diff')

def test_v2_on_file_diff_without_diff(callback_module):
    result = Mock()
    result._result = {}

    callback_module._display = Mock()
    callback_module._get_diff = Mock()

    callback_module.v2_on_file_diff(result)

    callback_module._display.display.assert_not_called()
    callback_module._get_diff.assert_not_called()
