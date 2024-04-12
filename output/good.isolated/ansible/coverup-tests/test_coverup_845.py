# file lib/ansible/playbook/task.py:335-340
# lines [335, 340]
# branches []

import pytest
from ansible.playbook.task import Task
from ansible.template import Templar

# Mock classes to avoid dependencies on the full Ansible framework
class Base:
    pass

class Conditional:
    pass

class Taggable:
    pass

class CollectionSearch:
    pass

# The actual test function
def test_post_validate_changed_when(mocker):
    # Create a mock Templar object
    templar_mock = mocker.MagicMock(spec=Templar)

    # Instantiate the Task object
    task = Task()

    # Define a test value for the 'changed_when' attribute
    test_value = "some_value"

    # Call the _post_validate_changed_when method
    result = task._post_validate_changed_when('changed_when', test_value, templar_mock)

    # Assert that the result is the same as the test value
    assert result == test_value

    # Assert that the templar was not used
    templar_mock.template.assert_not_called()

    # Clean up the mock
    mocker.stopall()
