# file: lib/ansible/plugins/callback/minimal.py:73-74
# asked: {"lines": [73, 74], "branches": []}
# gained: {"lines": [73, 74], "branches": []}

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.callback.minimal import CallbackModule
from ansible import constants as C

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_runner_on_unreachable(callback_module, mocker):
    # Mocking the result object
    result = Mock()
    result._host.get_name.return_value = 'test_host'
    result._result = {'key': 'value'}

    # Mocking the _display and _dump_results methods
    mock_display = mocker.patch.object(callback_module, '_display')
    mock_dump_results = mocker.patch.object(callback_module, '_dump_results', return_value='{"key": "value"}')

    # Call the method
    callback_module.v2_runner_on_unreachable(result)

    # Assertions
    mock_display.display.assert_called_once_with('test_host | UNREACHABLE! => {"key": "value"}', color=C.COLOR_UNREACHABLE)
    mock_dump_results.assert_called_once_with(result._result, indent=4)
