# file: lib/ansible/plugins/callback/default.py:170-188
# asked: {"lines": [174, 175, 179, 182, 184, 187, 188], "branches": [[174, 175], [174, 179], [179, 182], [179, 184], [187, 0], [187, 188]]}
# gained: {"lines": [174, 175, 179, 182, 184, 187, 188], "branches": [[174, 175], [174, 179], [179, 182], [179, 184], [187, 0], [187, 188]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.callback.default import CallbackModule

@pytest.fixture
def callback_module():
    module = CallbackModule()
    module._task_type_cache = {}
    module.check_mode_markers = False  # Mock attribute to avoid AttributeError
    return module

@pytest.fixture
def task():
    task = MagicMock()
    task._uuid = '1234-uuid'
    task.get_name.return_value = 'Test Task'
    task.no_log = False
    task.args = {}
    task.check_mode = False
    return task

@pytest.fixture
def play():
    play = MagicMock()
    return play

def test_task_start_with_prefix(callback_module, task, play):
    callback_module._play = play
    callback_module.display_skipped_hosts = True
    callback_module.display_ok_hosts = True

    callback_module._task_start(task, prefix='RUNNING HANDLER')

    assert callback_module._task_type_cache[task._uuid] == 'RUNNING HANDLER'

def test_task_start_strategy_free(callback_module, task, play):
    callback_module._play = play
    callback_module._play.strategy = 'free'
    callback_module.display_skipped_hosts = True
    callback_module.display_ok_hosts = True

    callback_module._task_start(task)

    assert callback_module._last_task_name is None

def test_task_start_strategy_host_pinned(callback_module, task, play):
    callback_module._play = play
    callback_module._play.strategy = 'host_pinned'
    callback_module.display_skipped_hosts = True
    callback_module.display_ok_hosts = True

    callback_module._task_start(task)

    assert callback_module._last_task_name is None

def test_task_start_other_strategy(callback_module, task, play):
    callback_module._play = play
    callback_module._play.strategy = 'linear'
    callback_module.display_skipped_hosts = True
    callback_module.display_ok_hosts = True

    with patch.object(callback_module, '_print_task_banner') as mock_print_task_banner:
        callback_module._task_start(task)

        assert callback_module._last_task_name == 'Test Task'
        mock_print_task_banner.assert_called_once_with(task)

def test_task_start_other_strategy_no_display(callback_module, task, play):
    callback_module._play = play
    callback_module._play.strategy = 'linear'
    callback_module.display_skipped_hosts = False
    callback_module.display_ok_hosts = False

    with patch.object(callback_module, '_print_task_banner') as mock_print_task_banner:
        callback_module._task_start(task)

        assert callback_module._last_task_name == 'Test Task'
        mock_print_task_banner.assert_not_called()
