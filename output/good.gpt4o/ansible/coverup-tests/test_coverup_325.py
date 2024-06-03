# file lib/ansible/plugins/callback/default.py:170-188
# lines [170, 174, 175, 179, 182, 184, 187, 188]
# branches ['174->175', '174->179', '179->182', '179->184', '187->exit', '187->188']

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.callback.default import CallbackModule

@pytest.fixture
def callback_module():
    module = CallbackModule()
    module._play = Mock()
    module._task_type_cache = {}
    module.display_skipped_hosts = False
    module.display_ok_hosts = False
    return module

def test_task_start_with_prefix(callback_module):
    task = Mock()
    task._uuid = '1234'
    prefix = 'RUNNING HANDLER'
    
    callback_module._task_start(task, prefix)
    
    assert callback_module._task_type_cache[task._uuid] == prefix

def test_task_start_with_strategy_free(callback_module):
    task = Mock()
    task.get_name.return_value = 'Test Task'
    
    callback_module._play.strategy = 'free'
    
    callback_module._task_start(task)
    
    assert callback_module._last_task_name is None

def test_task_start_with_strategy_host_pinned(callback_module):
    task = Mock()
    task.get_name.return_value = 'Test Task'
    
    callback_module._play.strategy = 'host_pinned'
    
    callback_module._task_start(task)
    
    assert callback_module._last_task_name is None

def test_task_start_with_other_strategy(callback_module, mocker):
    task = Mock()
    task.get_name.return_value = 'Test Task'
    
    callback_module._play.strategy = 'linear'
    
    callback_module.display_skipped_hosts = True
    callback_module.display_ok_hosts = True
    
    mock_print_task_banner = mocker.patch.object(callback_module, '_print_task_banner')
    
    callback_module._task_start(task)
    
    assert callback_module._last_task_name == 'Test Task'
    mock_print_task_banner.assert_called_once_with(task)
