# file lib/ansible/plugins/callback/default.py:101-134
# lines [103, 105, 106, 107, 108, 109, 110, 111, 113, 114, 116, 117, 119, 120, 122, 123, 125, 127, 128, 130, 132, 133, 134]
# branches ['105->106', '105->109', '106->107', '106->108', '109->110', '109->116', '110->111', '110->113', '116->117', '116->119', '119->120', '119->122', '127->128', '127->130', '132->133', '132->134']

import pytest
from ansible.plugins.callback import default
from ansible.executor.task_result import TaskResult
from ansible.playbook.task_include import TaskInclude
from ansible.playbook.task import Task
from unittest.mock import MagicMock, patch

# Mock the constants module to avoid import errors
class MockConstants:
    COLOR_CHANGED = 'yellow'
    COLOR_OK = 'green'

@pytest.fixture
def mock_display(mocker):
    with patch('ansible.utils.display.Display') as mock_display:
        yield mock_display

@pytest.fixture
def mock_task_result(mocker):
    fake_result = {
        'changed': False,
        'failed': False,
        'skipped': False,
        '_ansible_verbose_always': True,
        '_ansible_no_log': False,
    }
    task_result = TaskResult(
        host=mocker.MagicMock(),
        task=mocker.MagicMock(),
        return_data=fake_result,
        task_fields=mocker.MagicMock()
    )
    return task_result

@pytest.fixture
def callback_module(mock_display):
    callback = default.CallbackModule()
    callback._display = mock_display
    callback._last_task_banner = None
    callback.display_ok_hosts = True
    callback._run_is_verbose = MagicMock(return_value=False)
    callback._clean_results = MagicMock()
    callback._dump_results = MagicMock(return_value='dumped results')
    callback._handle_warnings = MagicMock()
    callback._process_items = MagicMock()
    callback._print_task_banner = MagicMock()
    callback.C = MockConstants
    return callback

def test_v2_runner_on_ok_include_task(callback_module, mock_task_result, mock_display):
    mock_task_result._task = TaskInclude()
    mock_task_result._task._uuid = 'test-uuid'
    callback_module._last_task_banner = 'test-uuid'
    callback_module.v2_runner_on_ok(mock_task_result)
    mock_display.display.assert_not_called()

def test_v2_runner_on_ok_changed(callback_module, mock_task_result, mock_display):
    mock_task_result._task = Task()
    mock_task_result._task._uuid = 'test-uuid'
    mock_task_result._result['changed'] = True
    callback_module._last_task_banner = 'different-uuid'
    callback_module.v2_runner_on_ok(mock_task_result)
    mock_display.display.assert_called_once_with('changed: [{}]'.format(mock_task_result._host.get_name()), color=MockConstants.COLOR_CHANGED)

def test_v2_runner_on_ok_ok(callback_module, mock_task_result, mock_display):
    mock_task_result._task = Task()
    mock_task_result._task._uuid = 'test-uuid'
    mock_task_result._result['changed'] = False
    callback_module._last_task_banner = 'different-uuid'
    callback_module.v2_runner_on_ok(mock_task_result)
    mock_display.display.assert_called_once_with('ok: [{}]'.format(mock_task_result._host.get_name()), color=MockConstants.COLOR_OK)

def test_v2_runner_on_ok_verbose(callback_module, mock_task_result, mock_display):
    mock_task_result._task = Task()
    mock_task_result._task._uuid = 'test-uuid'
    mock_task_result._result['changed'] = False
    callback_module._last_task_banner = 'different-uuid'
    callback_module._run_is_verbose = MagicMock(return_value=True)
    callback_module.v2_runner_on_ok(mock_task_result)
    mock_display.display.assert_called_once_with('ok: [{}] => dumped results'.format(mock_task_result._host.get_name()), color=MockConstants.COLOR_OK)

def test_v2_runner_on_ok_with_loop(callback_module, mock_task_result, mock_display):
    mock_task_result._task = Task()
    mock_task_result._task.loop = [1, 2, 3]
    mock_task_result._result['results'] = []
    callback_module.v2_runner_on_ok(mock_task_result)
    callback_module._process_items.assert_called_once_with(mock_task_result)
