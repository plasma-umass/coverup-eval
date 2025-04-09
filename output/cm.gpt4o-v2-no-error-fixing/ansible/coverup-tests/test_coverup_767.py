# file: lib/ansible/plugins/callback/default.py:306-315
# asked: {"lines": [307, 308, 309, 311, 312, 313, 314, 315], "branches": [[307, 0], [307, 308], [308, 309], [308, 311], [313, 314], [313, 315]]}
# gained: {"lines": [307, 308, 309, 311, 312, 313, 314, 315], "branches": [[307, 308], [308, 309], [313, 314]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.callback.default import CallbackModule
from ansible import constants as C

@pytest.fixture
def callback_module():
    module = CallbackModule()
    module.display_skipped_hosts = True
    module._last_task_banner = None
    module._display = MagicMock()
    return module

def test_v2_runner_item_on_skipped(callback_module):
    result = MagicMock()
    result._task._uuid = "unique-task-uuid"
    result._task.action = "some_action"
    result._host.get_name.return_value = "localhost"
    result._result = {"item": "test_item"}

    with patch.object(callback_module, '_print_task_banner') as mock_print_task_banner, \
         patch.object(callback_module, '_clean_results') as mock_clean_results, \
         patch.object(callback_module, '_get_item_label', return_value="test_item_label") as mock_get_item_label, \
         patch.object(callback_module, '_run_is_verbose', return_value=True) as mock_run_is_verbose, \
         patch.object(callback_module, '_dump_results', return_value="dumped_results") as mock_dump_results:

        callback_module.v2_runner_item_on_skipped(result)

        mock_print_task_banner.assert_called_once_with(result._task)
        mock_clean_results.assert_called_once_with(result._result, result._task.action)
        mock_get_item_label.assert_called_once_with(result._result)
        mock_run_is_verbose.assert_called_once_with(result)
        mock_dump_results.assert_called_once_with(result._result)
        callback_module._display.display.assert_called_once_with(
            "skipping: [localhost] => (item=test_item_label)  => dumped_results", color=C.COLOR_SKIP
        )
