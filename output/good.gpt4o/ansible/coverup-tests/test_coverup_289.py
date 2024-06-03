# file lib/ansible/plugins/callback/default.py:306-315
# lines [306, 307, 308, 309, 311, 312, 313, 314, 315]
# branches ['307->exit', '307->308', '308->309', '308->311', '313->314', '313->315']

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.callback.default import CallbackModule
from ansible.plugins.callback import CallbackBase
from ansible.utils.color import C

@pytest.fixture
def mock_result():
    result = MagicMock()
    result._task._uuid = 'task-uuid'
    result._task.action = 'action'
    result._host.get_name.return_value = 'host-name'
    result._result = {'item': 'item-value'}
    return result

@pytest.fixture
def callback_module():
    module = CallbackModule()
    module.display_skipped_hosts = True
    module._last_task_banner = None
    return module

def test_v2_runner_item_on_skipped(callback_module, mock_result, mocker):
    mocker.patch.object(callback_module, '_print_task_banner')
    mocker.patch.object(callback_module, '_clean_results')
    mocker.patch.object(callback_module, '_get_item_label', return_value='item-label')
    mocker.patch.object(callback_module, '_run_is_verbose', return_value=True)
    mocker.patch.object(callback_module, '_dump_results', return_value='dumped-results')
    mocker.patch.object(callback_module._display, 'display')

    callback_module.v2_runner_item_on_skipped(mock_result)

    callback_module._print_task_banner.assert_called_once_with(mock_result._task)
    callback_module._clean_results.assert_called_once_with(mock_result._result, mock_result._task.action)
    callback_module._get_item_label.assert_called_once_with(mock_result._result)
    callback_module._run_is_verbose.assert_called_once_with(mock_result)
    callback_module._dump_results.assert_called_once_with(mock_result._result)
    callback_module._display.display.assert_called_once_with(
        "skipping: [host-name] => (item=item-label)  => dumped-results", color=C.COLOR_SKIP
    )
