# file: lib/ansible/plugins/action/reboot.py:282-321
# asked: {"lines": [282, 283, 284, 285, 287, 288, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 303, 304, 305, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 321], "branches": [[284, 285], [284, 287], [290, 291], [290, 321], [293, 294], [293, 295], [297, 298], [297, 303], [305, 307], [305, 308], [308, 309], [308, 318]]}
# gained: {"lines": [282, 283, 284, 285, 287, 288, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 303, 304, 305, 308, 309, 310, 313, 314, 315, 316, 317, 318, 319, 321], "branches": [[284, 285], [290, 291], [290, 321], [293, 294], [297, 298], [297, 303], [305, 308], [308, 309]]}

import pytest
from unittest.mock import Mock, patch
from datetime import datetime, timedelta
from ansible.errors import AnsibleConnectionFailure
from ansible.module_utils._text import to_text
from ansible.plugins.action.reboot import ActionModule, TimedOutException
import random

class MockConnection:
    def reset(self):
        pass

class MockTask:
    action = "mock_action"

@pytest.fixture
def action_module():
    return ActionModule(MockTask(), MockConnection(), None, None, None, None)

def test_do_until_success_or_timeout_success(action_module):
    mock_action = Mock()
    action_module.do_until_success_or_timeout(mock_action, 5, "test_action", "test_distribution")
    mock_action.assert_called_once_with(distribution="test_distribution")

def test_do_until_success_or_timeout_timeout(action_module):
    mock_action = Mock(side_effect=Exception("Test Exception"))
    with pytest.raises(TimedOutException):
        action_module.do_until_success_or_timeout(mock_action, 1, "test_action", "test_distribution")

def test_do_until_success_or_timeout_connection_failure(action_module):
    mock_action = Mock(side_effect=AnsibleConnectionFailure("Connection failed"))
    action_module._connection.reset = Mock()
    with pytest.raises(TimedOutException):
        action_module.do_until_success_or_timeout(mock_action, 1, "test_action", "test_distribution")
    action_module._connection.reset.assert_called()

def test_do_until_success_or_timeout_random_sleep(action_module, monkeypatch):
    mock_action = Mock(side_effect=Exception("Test Exception"))
    monkeypatch.setattr(random, 'randint', lambda a, b: 500)
    with pytest.raises(TimedOutException):
        action_module.do_until_success_or_timeout(mock_action, 1, "test_action", "test_distribution")

def test_do_until_success_or_timeout_to_text(action_module):
    mock_action = Mock(side_effect=Exception("Test Exception"))
    with patch('ansible.plugins.action.reboot.to_text', side_effect=to_text) as mock_to_text:
        with pytest.raises(TimedOutException):
            action_module.do_until_success_or_timeout(mock_action, 1, "test_action", "test_distribution")
        assert mock_to_text.called

def test_do_until_success_or_timeout_display_debug(action_module):
    mock_action = Mock(side_effect=Exception("Test Exception"))
    with patch('ansible.plugins.action.reboot.display.debug') as mock_debug:
        with pytest.raises(TimedOutException):
            action_module.do_until_success_or_timeout(mock_action, 1, "test_action", "test_distribution")
        assert mock_debug.called
