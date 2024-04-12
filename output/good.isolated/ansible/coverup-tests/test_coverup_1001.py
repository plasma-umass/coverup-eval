# file lib/ansible/plugins/callback/minimal.py:73-74
# lines [73, 74]
# branches []

import pytest
from ansible.plugins.callback import minimal
from ansible.executor.task_result import TaskResult
from ansible.playbook.task import Task
from ansible.parsing.dataloader import DataLoader
from ansible.inventory.host import Host
from ansible.inventory.manager import InventoryManager
from ansible.vars.manager import VariableManager
from unittest.mock import MagicMock, PropertyMock

# Define a custom pytest fixture to set up the environment for the test
@pytest.fixture
def minimal_callback(mocker):
    # Create the callback plugin instance
    callback_plugin = minimal.CallbackModule()

    # Mock the display object to capture the output
    callback_plugin._display = MagicMock()

    # Mock the verbosity to avoid the TypeError
    verbosity = PropertyMock(return_value=0)
    type(callback_plugin._display).verbosity = verbosity

    return callback_plugin

# Define the test function
def test_v2_runner_on_unreachable(minimal_callback):
    # Set up the necessary objects to simulate an unreachable host
    host = Host(name='testhost')
    task = Task()
    loader = DataLoader()
    inventory = InventoryManager(loader=loader)
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    result = TaskResult(host=host, task=task, return_data={'unreachable': True})

    # Call the method we want to test
    minimal_callback.v2_runner_on_unreachable(result)

    # Assert that the display method was called with the expected message
    expected_message = "%s | UNREACHABLE! => %s" % (host.get_name(), minimal_callback._dump_results(result._result, indent=4))
    minimal_callback._display.display.assert_called_once_with(expected_message, color=minimal.C.COLOR_UNREACHABLE)
