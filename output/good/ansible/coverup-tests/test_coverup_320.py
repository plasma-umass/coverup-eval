# file lib/ansible/plugins/callback/default.py:306-315
# lines [306, 307, 308, 309, 311, 312, 313, 314, 315]
# branches ['307->exit', '307->308', '308->309', '308->311', '313->314', '313->315']

import pytest
from ansible.plugins.callback.default import CallbackModule
from ansible.executor.task_result import TaskResult
from ansible.playbook.task import Task
from ansible.parsing.dataloader import DataLoader
from ansible.inventory.host import Host
from ansible.inventory.manager import InventoryManager
from unittest.mock import MagicMock, patch

# Define a test case for the v2_runner_item_on_skipped method
def test_v2_runner_item_on_skipped(mocker):
    # Mock the necessary components
    mocker.patch('ansible.plugins.callback.default.C')
    display_mock = MagicMock()
    task_mock = MagicMock()
    task_mock._uuid = 'test_uuid'
    task_mock.action = 'test_action'
    task_mock.get_name = MagicMock(return_value='test_task')
    task_mock.args = {'arg1': 'value1'}
    task_mock.no_log = False
    result_mock = MagicMock(spec=TaskResult)
    result_mock._task = task_mock
    result_mock._host = Host(name='test_host')
    result_mock._result = {'skipped': True, 'item': 'test_item'}

    # Create an instance of the CallbackModule
    callback_module = CallbackModule()
    callback_module._display = display_mock
    callback_module.display_skipped_hosts = True
    callback_module._last_task_banner = None
    callback_module._run_is_verbose = MagicMock(return_value=False)
    callback_module._print_task_banner = MagicMock()
    callback_module._clean_results = MagicMock()
    callback_module._get_item_label = MagicMock(return_value='test_item')
    callback_module._dump_results = MagicMock(return_value='dumped_results')
    callback_module.check_mode_markers = True

    # Call the method under test
    callback_module.v2_runner_item_on_skipped(result_mock)

    # Assert that the display method was called with the expected message
    expected_msg = "skipping: [test_host] => (item=test_item) "
    display_mock.display.assert_called_once_with(expected_msg, color=mocker.ANY)

    # Clean up / reset mocks to not affect other tests
    mocker.stopall()

# Run the test
def run_module_tests():
    pytest.main([__file__, '--tb=native', '-v', '-s'])

if __name__ == "__main__":
    run_module_tests()
