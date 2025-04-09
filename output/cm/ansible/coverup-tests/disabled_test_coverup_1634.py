# file lib/ansible/playbook/task.py:266-271
# lines [267, 268, 269, 270, 271]
# branches []

import pytest
from ansible.errors import AnsibleParserError
from ansible.playbook.task import Task
from ansible.playbook.base import Base

# Mocking the Base class to raise AnsibleParserError when _validate_attributes is called
class MockedBase(Base):
    def _validate_attributes(self, ds):
        raise AnsibleParserError("Test error")

# Injecting the mocked base class into the Task's inheritance to replace the original Base
Task.__bases__ = (MockedBase,) + Task.__bases__[1:]

def test_task_validate_attributes_raises_exception_with_custom_message(mocker):
    # Arrange
    task = Task()
    data = {}

    # Act & Assert
    with pytest.raises(AnsibleParserError) as exc_info:
        task._validate_attributes(data)

    # Cleanup
    Task.__bases__ = (Base,) + Task.__bases__[1:]

    # Verify the exception message has been augmented
    assert "This error can be suppressed as a warning using the \"invalid_task_attribute_failed\" configuration" in str(exc_info.value)
