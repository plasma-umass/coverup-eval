# file: lib/ansible/plugins/action/wait_for_connection.py:45-61
# asked: {"lines": [45, 46, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 61], "branches": [[49, 50], [49, 61], [52, 53], [52, 54], [57, 58], [57, 59]]}
# gained: {"lines": [45, 46, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 61], "branches": [[49, 50], [49, 61], [52, 53], [57, 58]]}

import pytest
from unittest.mock import Mock, patch
from datetime import datetime, timedelta
from ansible.plugins.action.wait_for_connection import ActionModule, TimedOutException
from ansible.playbook.task import Task
from ansible.playbook.play_context import PlayContext
from ansible.plugins.loader import PluginLoader
from ansible.template import Templar

@pytest.fixture
def action_module():
    task = Mock(spec=Task)
    connection = Mock()
    play_context = Mock(spec=PlayContext)
    loader = Mock(spec=PluginLoader)
    templar = Mock(spec=Templar)
    shared_loader_obj = Mock()
    return ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)

def test_do_until_success_or_timeout_success(action_module):
    mock_what = Mock()
    mock_what_desc = "test connection"
    
    action_module.do_until_success_or_timeout(mock_what, 5, 1, mock_what_desc)
    
    mock_what.assert_called_once_with(1)

def test_do_until_success_or_timeout_timeout(action_module):
    mock_what = Mock(side_effect=Exception("connection failed"))
    mock_what_desc = "test connection"
    
    with pytest.raises(TimedOutException) as excinfo:
        action_module.do_until_success_or_timeout(mock_what, 1, 1, mock_what_desc, sleep=0.1)
    
    assert "timed out waiting for test connection: connection failed" in str(excinfo.value)
    assert mock_what.call_count > 1

def test_do_until_success_or_timeout_with_debug(action_module, monkeypatch):
    mock_what = Mock(side_effect=[Exception("connection failed"), None])
    mock_what_desc = "test connection"
    
    mock_display = Mock()
    monkeypatch.setattr("ansible.plugins.action.wait_for_connection.display", mock_display)
    
    action_module.do_until_success_or_timeout(mock_what, 5, 1, mock_what_desc, sleep=0.1)
    
    assert mock_what.call_count == 2
    mock_display.debug.assert_any_call("wait_for_connection: test connection fail (expected), retrying in 0 seconds...")
    mock_display.debug.assert_any_call("wait_for_connection: test connection success")
