# file lib/ansible/playbook/task.py:349-354
# lines [349, 354]
# branches []

import pytest
from ansible.playbook.task import Task
from ansible.template import Templar

# Mocking the necessary classes to avoid side effects on other tests
class MockBase:
    pass

class MockConditional:
    pass

class MockTaggable:
    pass

class MockCollectionSearch:
    pass

# Creating a new Task class for testing purposes
class TestTask(MockBase, MockConditional, MockTaggable, MockCollectionSearch, Task):
    pass

# Test function to cover _post_validate_until method
def test_post_validate_until(mocker):
    # Setup
    templar_mock = mocker.MagicMock(spec=Templar)
    task = TestTask()

    # Test the _post_validate_until method directly
    test_value = "test_until_value"
    result = task._post_validate_until('until', test_value, templar_mock)

    # Assert that the result is the same as the input value
    assert result == test_value

    # Assert that templar was not used
    templar_mock.template.assert_not_called()
