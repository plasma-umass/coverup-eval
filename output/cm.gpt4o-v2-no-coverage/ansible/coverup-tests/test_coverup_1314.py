# file: lib/ansible/plugins/callback/default.py:170-188
# asked: {"lines": [], "branches": [[187, 0]]}
# gained: {"lines": [], "branches": [[187, 0]]}

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.callback.default import CallbackModule

@pytest.fixture
def callback_module():
    module = CallbackModule()
    module._play = Mock()
    module.display_skipped_hosts = False
    module.display_ok_hosts = False
    return module

def test_task_start_with_prefix(callback_module):
    task = Mock()
    task._uuid = "1234"
    prefix = "RUNNING HANDLER"
    
    callback_module._task_start(task, prefix)
    
    assert callback_module._task_type_cache[task._uuid] == prefix

def test_task_start_without_prefix(callback_module):
    task = Mock()
    task._uuid = "1234"
    
    callback_module._task_start(task)
    
    assert task._uuid not in callback_module._task_type_cache

def test_task_start_with_free_strategy(callback_module):
    task = Mock()
    task._uuid = "1234"
    callback_module._play.strategy = 'free'
    
    callback_module._task_start(task)
    
    assert callback_module._last_task_name is None

def test_task_start_with_host_pinned_strategy(callback_module):
    task = Mock()
    task._uuid = "1234"
    callback_module._play.strategy = 'host_pinned'
    
    callback_module._task_start(task)
    
    assert callback_module._last_task_name is None

def test_task_start_with_other_strategy(callback_module):
    task = Mock()
    task._uuid = "1234"
    task.get_name.return_value = " Task Name "
    callback_module._play.strategy = 'linear'
    
    callback_module._task_start(task)
    
    assert callback_module._last_task_name == "Task Name"

@patch.object(CallbackModule, '_print_task_banner')
def test_task_start_with_display_flags(mock_print_task_banner, callback_module):
    task = Mock()
    task._uuid = "1234"
    task.get_name.return_value = " Task Name "
    callback_module._play.strategy = 'linear'
    callback_module.display_skipped_hosts = True
    callback_module.display_ok_hosts = True
    
    callback_module._task_start(task)
    
    mock_print_task_banner.assert_called_once_with(task)
