# file lib/ansible/plugins/action/include_vars.py:18-26
# lines [18, 20, 22, 23, 24, 25]
# branches []

import pytest
from ansible.plugins.action.include_vars import ActionModule
from ansible.utils.vars import load_extra_vars
from ansible.utils.vars import load_options_vars
from ansible.executor.task_executor import TaskExecutor
from ansible.executor.task_result import TaskResult
from ansible.playbook.task import Task
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.inventory.manager import InventoryManager
from ansible.vars.manager import VariableManager
from ansible.parsing.dataloader import DataLoader
from unittest.mock import MagicMock, patch

# Since the provided code snippet is just a class definition and does not contain any executable code,
# I will create a test that instantiates the ActionModule and checks its attributes.
# This test assumes that the ActionModule class is part of a larger codebase where it is used properly.

@pytest.fixture
def action_module():
    # Mocking the necessary components to create an instance of ActionModule
    mock_loader = DataLoader()
    mock_task = Task()
    mock_connection = MagicMock()
    mock_play_context = MagicMock()
    mock_queue_manager = MagicMock()
    mock_variable_manager = VariableManager(loader=mock_loader, inventory=InventoryManager(loader=mock_loader))

    action_module_instance = ActionModule(task=mock_task, connection=mock_connection, play_context=mock_play_context, loader=mock_loader, templar=None, shared_loader_obj=None)
    return action_module_instance

def test_action_module_attributes(action_module):
    # Test the attributes of the ActionModule class
    assert action_module.TRANSFERS_FILES == False
    assert action_module.VALID_FILE_EXTENSIONS == ['yaml', 'yml', 'json']
    assert action_module.VALID_DIR_ARGUMENTS == ['dir', 'depth', 'files_matching', 'ignore_files', 'extensions', 'ignore_unknown_extensions']
    assert action_module.VALID_FILE_ARGUMENTS == ['file', '_raw_params']
    assert action_module.VALID_ALL == ['name', 'hash_behaviour']
