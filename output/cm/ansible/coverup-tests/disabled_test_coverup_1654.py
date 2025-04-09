# file lib/ansible/playbook/task_include.py:53-61
# lines [55, 56, 57, 58, 61]
# branches []

import pytest
from ansible.playbook.task_include import TaskInclude
from ansible.errors import AnsibleError

# Assuming the existence of a TaskInclude class with the given method signature

def test_task_include_load_with_invalid_data(mocker):
    # Mock the necessary components
    block = mocker.MagicMock()
    role = mocker.MagicMock()
    task_include = mocker.MagicMock()
    variable_manager = mocker.MagicMock()
    loader = mocker.MagicMock()

    # Mock the load_data method to raise an AnsibleError
    mocker.patch.object(TaskInclude, 'load_data', side_effect=AnsibleError)

    # Mock the check_options method to simply return its argument
    mocker.patch.object(TaskInclude, 'check_options', side_effect=lambda x, y: x)

    # Define invalid data that would cause load_data to raise an AnsibleError
    invalid_data = {'invalid': 'data'}

    # Test that the load method raises an AnsibleError with invalid data
    with pytest.raises(AnsibleError):
        TaskInclude.load(invalid_data, block=block, role=role, task_include=task_include,
                         variable_manager=variable_manager, loader=loader)

    # Assert that load_data was called with the correct arguments
    TaskInclude.load_data.assert_called_once_with(invalid_data, variable_manager=variable_manager, loader=loader)

    # Assert that check_options was not called due to the raised AnsibleError
    TaskInclude.check_options.assert_not_called()
