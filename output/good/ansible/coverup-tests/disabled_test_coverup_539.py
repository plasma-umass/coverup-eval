# file lib/ansible/playbook/task_include.py:53-61
# lines [53, 54, 55, 56, 57, 58, 61]
# branches []

import pytest
from ansible.playbook.task_include import TaskInclude
from ansible.errors import AnsibleError

# Mock classes to support the test
class MockBlock:
    pass

class MockRole:
    pass

class MockTaskInclude:
    pass

class MockVariableManager:
    pass

class MockLoader:
    pass

# Test function to improve coverage
def test_task_include_load(mocker):
    # Mock the necessary methods and attributes
    mock_block = MockBlock()
    mock_role = MockRole()
    mock_task_include = MockTaskInclude()
    mock_variable_manager = MockVariableManager()
    mock_loader = MockLoader()
    
    # Mock the check_options and load_data methods
    mocker.patch.object(TaskInclude, 'check_options', return_value='mocked_task')
    mocker.patch.object(TaskInclude, 'load_data', return_value={})

    # Call the static method load
    task = TaskInclude.load(
        data={},
        block=mock_block,
        role=mock_role,
        task_include=mock_task_include,
        variable_manager=mock_variable_manager,
        loader=mock_loader
    )

    # Assertions to verify postconditions
    assert task == 'mocked_task'
    TaskInclude.check_options.assert_called_once()
    TaskInclude.load_data.assert_called_once_with({}, variable_manager=mock_variable_manager, loader=mock_loader)
