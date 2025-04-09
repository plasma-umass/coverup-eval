# file lib/ansible/plugins/callback/junit.py:307-308
# lines [307, 308]
# branches []

import pytest
from ansible.plugins.callback.junit import CallbackModule
from ansible.playbook.task_include import TaskInclude
from unittest.mock import MagicMock

# Define a test case for the v2_playbook_on_include method
def test_v2_playbook_on_include(mocker):
    # Create an instance of the CallbackModule
    callback_module = CallbackModule()

    # Mock the _finish_task method to verify it's being called correctly
    mocker.patch.object(callback_module, '_finish_task')

    # Create a mock included_file object
    included_file = MagicMock(spec=TaskInclude)
    included_file._filename = '/path/to/included/file.yml'

    # Call the method under test
    callback_module.v2_playbook_on_include(included_file)

    # Assert that _finish_task was called with the correct arguments
    callback_module._finish_task.assert_called_once_with('included', included_file)

# Run the test function if this file is executed directly (not recommended)
if __name__ == "__main__":
    pytest.main([__file__])
