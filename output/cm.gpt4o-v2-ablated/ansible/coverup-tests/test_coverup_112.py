# file: lib/ansible/plugins/callback/default.py:170-188
# asked: {"lines": [170, 174, 175, 179, 182, 184, 187, 188], "branches": [[174, 175], [174, 179], [179, 182], [179, 184], [187, 0], [187, 188]]}
# gained: {"lines": [170, 174, 175, 179, 182, 184, 187, 188], "branches": [[174, 175], [174, 179], [179, 182], [179, 184], [187, 188]]}

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.callback.default import CallbackModule

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_task_start_with_prefix(callback_module):
    task = Mock()
    task._uuid = '1234'
    prefix = 'RUNNING HANDLER'
    
    callback_module._task_type_cache = {}
    callback_module._play = Mock()
    callback_module._play.strategy = 'linear'
    callback_module.display_skipped_hosts = True
    callback_module.display_ok_hosts = True
    
    with patch.object(callback_module, '_print_task_banner') as mock_print_task_banner:
        callback_module._task_start(task, prefix)
        assert callback_module._task_type_cache[task._uuid] == prefix
        assert callback_module._last_task_name == task.get_name().strip()
        mock_print_task_banner.assert_called_once_with(task)

def test_task_start_without_prefix(callback_module):
    task = Mock()
    task._uuid = '1234'
    
    callback_module._task_type_cache = {}
    callback_module._play = Mock()
    callback_module._play.strategy = 'linear'
    callback_module.display_skipped_hosts = True
    callback_module.display_ok_hosts = True
    
    with patch.object(callback_module, '_print_task_banner') as mock_print_task_banner:
        callback_module._task_start(task)
        assert task._uuid not in callback_module._task_type_cache
        assert callback_module._last_task_name == task.get_name().strip()
        mock_print_task_banner.assert_called_once_with(task)

def test_task_start_free_strategy(callback_module):
    task = Mock()
    task._uuid = '1234'
    
    callback_module._task_type_cache = {}
    callback_module._play = Mock()
    callback_module._play.strategy = 'free'
    callback_module.display_skipped_hosts = True
    callback_module.display_ok_hosts = True
    
    with patch.object(callback_module, '_print_task_banner') as mock_print_task_banner:
        callback_module._task_start(task)
        assert task._uuid not in callback_module._task_type_cache
        assert callback_module._last_task_name is None
        mock_print_task_banner.assert_not_called()

def test_task_start_host_pinned_strategy(callback_module):
    task = Mock()
    task._uuid = '1234'
    
    callback_module._task_type_cache = {}
    callback_module._play = Mock()
    callback_module._play.strategy = 'host_pinned'
    callback_module.display_skipped_hosts = True
    callback_module.display_ok_hosts = True
    
    with patch.object(callback_module, '_print_task_banner') as mock_print_task_banner:
        callback_module._task_start(task)
        assert task._uuid not in callback_module._task_type_cache
        assert callback_module._last_task_name is None
        mock_print_task_banner.assert_not_called()
