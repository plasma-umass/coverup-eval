# file: lib/ansible/plugins/action/reboot.py:282-321
# asked: {"lines": [282, 283, 284, 285, 287, 288, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 303, 304, 305, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 321], "branches": [[284, 285], [284, 287], [290, 291], [290, 321], [293, 294], [293, 295], [297, 298], [297, 303], [305, 307], [305, 308], [308, 309], [308, 318]]}
# gained: {"lines": [282, 283, 284, 285, 287, 288, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 303, 304, 305, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 321], "branches": [[284, 285], [290, 291], [290, 321], [293, 294], [297, 298], [297, 303], [305, 308], [308, 309]]}

import pytest
from unittest.mock import Mock, patch
from datetime import datetime, timedelta
import random
from ansible.errors import AnsibleConnectionFailure
from ansible.module_utils._text import to_text
from ansible.plugins.action.reboot import ActionModule, TimedOutException

@pytest.fixture
def action_module():
    task = Mock()
    connection = Mock()
    play_context = Mock()
    loader = Mock()
    templar = Mock()
    shared_loader_obj = Mock()
    return ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)

def test_do_until_success_or_timeout_success(action_module):
    action = Mock()
    action_module.do_until_success_or_timeout(action, 5, "test action", "test distribution")
    action.assert_called_once_with(distribution="test distribution")

def test_do_until_success_or_timeout_timeout(action_module):
    action = Mock(side_effect=Exception("test exception"))
    with pytest.raises(TimedOutException, match="Timed out waiting for test action"):
        action_module.do_until_success_or_timeout(action, 1, "test action", "test distribution")

def test_do_until_success_or_timeout_connection_failure(action_module):
    action = Mock(side_effect=AnsibleConnectionFailure("connection failure"))
    action_module._connection.reset = Mock(side_effect=AnsibleConnectionFailure("reset failure"))
    with pytest.raises(TimedOutException, match="Timed out waiting for test action"):
        action_module.do_until_success_or_timeout(action, 1, "test action", "test distribution")
    assert action_module._connection.reset.call_count > 0

def test_do_until_success_or_timeout_random_sleep(action_module, monkeypatch):
    action = Mock(side_effect=Exception("test exception"))
    monkeypatch.setattr(random, 'randint', lambda a, b: 500)
    with pytest.raises(TimedOutException, match="Timed out waiting for test action"):
        action_module.do_until_success_or_timeout(action, 1, "test action", "test distribution")
    action.assert_called()

def test_do_until_success_or_timeout_index_error(action_module):
    def action(**kwargs):
        raise Exception("test exception")
    with patch('ansible.plugins.action.reboot.to_text', side_effect=lambda e: ""):
        with pytest.raises(TimedOutException, match="Timed out waiting for test action"):
            action_module.do_until_success_or_timeout(action, 1, "test action", "test distribution")
