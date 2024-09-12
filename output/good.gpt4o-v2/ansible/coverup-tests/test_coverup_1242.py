# file: lib/ansible/plugins/callback/default.py:306-315
# asked: {"lines": [], "branches": [[307, 0], [308, 311], [313, 315]]}
# gained: {"lines": [], "branches": [[307, 0], [308, 311], [313, 315]]}

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.callback.default import CallbackModule
from ansible import constants as C

@pytest.fixture
def callback_module():
    module = CallbackModule()
    module._last_task_banner = None
    module.display_skipped_hosts = True
    module._display = Mock()
    return module

def test_v2_runner_item_on_skipped_display_skipped_hosts(callback_module):
    result = Mock()
    result._task._uuid = "1234"
    result._task.action = "test_action"
    result._result = {"_ansible_verbose_always": True}
    result._host.get_name.return_value = "localhost"
    result._task.get_name.return_value = "test_task"

    callback_module._last_task_banner = "5678"
    callback_module._run_is_verbose = Mock(return_value=True)
    callback_module._dump_results = Mock(return_value="dumped_results")
    callback_module._get_item_label = Mock(return_value="item_label")
    callback_module._print_task_banner = Mock()
    callback_module._clean_results = Mock()

    callback_module.v2_runner_item_on_skipped(result)

    callback_module._print_task_banner.assert_called_once_with(result._task)
    callback_module._clean_results.assert_called_once_with(result._result, result._task.action)
    callback_module._display.display.assert_called_once_with(
        "skipping: [localhost] => (item=item_label)  => dumped_results", color=C.COLOR_SKIP
    )

def test_v2_runner_item_on_skipped_no_display_skipped_hosts(callback_module):
    callback_module.display_skipped_hosts = False
    result = Mock()
    callback_module.v2_runner_item_on_skipped(result)
    callback_module._display.display.assert_not_called()

def test_v2_runner_item_on_skipped_same_task_banner(callback_module):
    result = Mock()
    result._task._uuid = "1234"
    result._task.action = "test_action"
    result._result = {"_ansible_verbose_always": True}
    result._host.get_name.return_value = "localhost"
    result._task.get_name.return_value = "test_task"

    callback_module._last_task_banner = "1234"
    callback_module._run_is_verbose = Mock(return_value=False)
    callback_module._dump_results = Mock(return_value="dumped_results")
    callback_module._get_item_label = Mock(return_value="item_label")
    callback_module._print_task_banner = Mock()
    callback_module._clean_results = Mock()

    callback_module.v2_runner_item_on_skipped(result)

    callback_module._print_task_banner.assert_not_called()
    callback_module._clean_results.assert_called_once_with(result._result, result._task.action)
    callback_module._display.display.assert_called_once_with(
        "skipping: [localhost] => (item=item_label) ", color=C.COLOR_SKIP
    )
