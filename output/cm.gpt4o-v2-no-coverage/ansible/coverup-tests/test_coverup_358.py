# file: lib/ansible/plugins/callback/default.py:170-188
# asked: {"lines": [170, 174, 175, 179, 182, 184, 187, 188], "branches": [[174, 175], [174, 179], [179, 182], [179, 184], [187, 0], [187, 188]]}
# gained: {"lines": [170, 174, 175, 179, 182, 184, 187, 188], "branches": [[174, 175], [174, 179], [179, 182], [179, 184], [187, 188]]}

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.callback.default import CallbackModule

@pytest.fixture
def callback_module():
    cb = CallbackModule()
    cb._task_type_cache = {}
    cb._play = Mock()
    cb.display_skipped_hosts = True
    cb.display_ok_hosts = True
    cb.check_mode_markers = True
    cb._display = Mock()
    cb._display.verbosity = 1
    return cb

def test_task_start_with_prefix(callback_module):
    task = Mock()
    task._uuid = '1234'
    prefix = 'RUNNING HANDLER'
    
    callback_module._task_start(task, prefix)
    
    assert callback_module._task_type_cache[task._uuid] == prefix

def test_task_start_strategy_free(callback_module):
    task = Mock()
    callback_module._play.strategy = 'free'
    
    callback_module._task_start(task)
    
    assert callback_module._last_task_name is None

def test_task_start_strategy_host_pinned(callback_module):
    task = Mock()
    callback_module._play.strategy = 'host_pinned'
    
    callback_module._task_start(task)
    
    assert callback_module._last_task_name is None

def test_task_start_other_strategy(callback_module):
    task = Mock()
    task.get_name.return_value = ' Test Task '
    callback_module._play.strategy = 'linear'
    
    callback_module._task_start(task)
    
    assert callback_module._last_task_name == 'Test Task'

@patch.object(CallbackModule, '_print_task_banner')
def test_task_start_print_task_banner(mock_print_task_banner, callback_module):
    task = Mock()
    task.get_name.return_value = ' Test Task '
    callback_module._play.strategy = 'linear'
    
    callback_module._task_start(task)
    
    mock_print_task_banner.assert_called_once_with(task)
