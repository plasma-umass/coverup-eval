# file lib/ansible/playbook/task_include.py:53-61
# lines [55, 56, 57, 58, 61]
# branches []

import pytest
from ansible.playbook.task_include import TaskInclude
from ansible.errors import AnsibleError

# Assuming the existence of a TaskInclude class with the provided method signature

class TestTaskInclude:
    def test_load_with_invalid_data(self, mocker):
        # Mocking the necessary objects and methods
        block = mocker.MagicMock()
        role = mocker.MagicMock()
        task_include = mocker.MagicMock()
        variable_manager = mocker.MagicMock()
        loader = mocker.MagicMock()
        invalid_data = {'invalid': 'data'}

        # Mocking the load_data method to return invalid data
        mocker.patch.object(TaskInclude, 'load_data', return_value=invalid_data)

        # Mocking the check_options method to raise an AnsibleError
        mocker.patch.object(TaskInclude, 'check_options', side_effect=AnsibleError)

        # Running the test
        with pytest.raises(AnsibleError):
            TaskInclude.load(invalid_data, block=block, role=role, task_include=task_include,
                             variable_manager=variable_manager, loader=loader)

        # No need for assertions as the test is expected to raise an AnsibleError

        # Clean up is handled by pytest-mock through the mocker fixture
