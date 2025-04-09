# file: lib/ansible/plugins/action/reboot.py:97-102
# asked: {"lines": [97, 99, 100, 101, 102], "branches": [[100, 101], [100, 102]]}
# gained: {"lines": [97, 99, 100, 101, 102], "branches": [[100, 101], [100, 102]]}

import pytest
from unittest.mock import Mock
from ansible.plugins.action.reboot import ActionModule

@pytest.fixture
def mock_task():
    task = Mock()
    task.args = {}
    return task

@pytest.fixture
def action_module(mock_task):
    return ActionModule(task=mock_task, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

def test_check_delay_positive_value(action_module, mock_task):
    mock_task.args = {'delay': 10}
    result = action_module._check_delay('delay', 5)
    assert result == 10

def test_check_delay_default_value(action_module, mock_task):
    mock_task.args = {}
    result = action_module._check_delay('delay', 5)
    assert result == 5

def test_check_delay_negative_value(action_module, mock_task):
    mock_task.args = {'delay': -10}
    result = action_module._check_delay('delay', 5)
    assert result == 0

def test_check_delay_sec_key(action_module, mock_task):
    mock_task.args = {'delay_sec': 20}
    result = action_module._check_delay('delay', 5)
    assert result == 20
