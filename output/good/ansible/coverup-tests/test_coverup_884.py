# file lib/ansible/playbook/task.py:342-347
# lines [342, 347]
# branches []

import pytest
from unittest.mock import MagicMock
from ansible.playbook.task import Task

# Mock classes to avoid side effects and dependencies
class MockBase:
    pass

class MockConditional:
    pass

class MockTaggable:
    pass

class MockCollectionSearch:
    pass

# Injecting the mock classes into Task to isolate the test environment
Task.__bases__ = (MockBase, MockConditional, MockTaggable, MockCollectionSearch)

@pytest.fixture
def templar():
    # Mock Templar object
    return MagicMock()

@pytest.fixture
def task():
    # Task instance with mocked dependencies
    return Task()

def test_post_validate_failed_when(task, templar):
    # Test value to be used for the 'failed_when' attribute
    test_value = ['some_condition']

    # Call the method we want to test
    result = task._post_validate_failed_when('failed_when', test_value, templar)

    # Assert that the result is the same as the input value, as the method should not modify it
    assert result == test_value

    # Verify that the templar was not used, as the method should not template the value
    templar.template.assert_not_called()
