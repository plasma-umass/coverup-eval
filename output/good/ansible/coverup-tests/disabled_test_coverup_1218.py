# file lib/ansible/playbook/task.py:378-392
# lines [379, 381, 382, 383, 385, 386, 387, 389, 390, 392]
# branches ['382->383', '382->385', '386->387', '386->389']

import pytest
from ansible.playbook.task import Task

# Mock classes to simulate the behavior of Base, Conditional, Taggable, CollectionSearch
class Base:
    def copy(self):
        return self

class Conditional(Base):
    pass

class Taggable(Conditional):
    pass

class CollectionSearch(Taggable):
    pass

# Mock class to simulate the behavior of the parent and role objects
class MockParent:
    def copy(self, exclude_tasks=False):
        return self

class MockRole:
    pass

# The actual test function
def test_task_copy(mocker):
    # Create a Task instance with a mock parent and role
    task = Task()
    task._parent = MockParent()
    task._role = MockRole()
    task.implicit = False
    task.resolved_action = 'some_action'

    # Mock the copy method of the parent to ensure it gets called
    mocker.patch.object(MockParent, 'copy', return_value=MockParent())

    # Call the copy method on the task
    new_task = task.copy()

    # Assertions to check the postconditions
    assert new_task._parent is not None, "The parent should be copied"
    assert new_task._role is not None, "The role should be copied"
    assert new_task.implicit == task.implicit, "The implicit attribute should be copied"
    assert new_task.resolved_action == task.resolved_action, "The resolved_action attribute should be copied"

    # Now test with exclude_parent=True
    new_task_excluded_parent = task.copy(exclude_parent=True)
    assert new_task_excluded_parent._parent is None, "The parent should not be copied when exclude_parent=True"

    # Clean up after the test
    mocker.stopall()
