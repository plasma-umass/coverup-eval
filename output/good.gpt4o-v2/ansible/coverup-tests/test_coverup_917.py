# file: lib/ansible/plugins/callback/minimal.py:73-74
# asked: {"lines": [73, 74], "branches": []}
# gained: {"lines": [73, 74], "branches": []}

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.callback import minimal
from ansible import constants as C

@pytest.fixture
def callback_module():
    return minimal.CallbackModule()

def test_v2_runner_on_unreachable(callback_module):
    result = Mock()
    result._host.get_name.return_value = 'test_host'
    result._result = {'msg': 'unreachable'}

    with patch.object(callback_module._display, 'display') as mock_display:
        callback_module.v2_runner_on_unreachable(result)
        mock_display.assert_called_once_with(
            'test_host | UNREACHABLE! => {\n    "msg": "unreachable"\n}', 
            color=C.COLOR_UNREACHABLE
        )
