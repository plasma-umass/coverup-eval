# file lib/ansible/playbook/task.py:273-285
# lines [279, 280, 282, 283, 285]
# branches ['279->280', '279->282', '282->283', '282->285']

import pytest
from ansible.playbook.task import Task
from ansible.template import Templar
from ansible.playbook.base import Base
from ansible.playbook.conditional import Conditional
from ansible.playbook.taggable import Taggable
from ansible.playbook.collectionsearch import CollectionSearch
from ansible.playbook.collectionsearch import AnsibleCollectionConfig

# Mock classes to simulate the behavior of the parent and to check if post_validate is called
class MockParent(Base, Conditional, Taggable, CollectionSearch):
    def post_validate(self, templar):
        self.called = True

@pytest.fixture
def templar():
    return Templar(loader=None)

@pytest.fixture
def mock_parent(mocker):
    parent = MockParent()
    mocker.spy(parent, 'post_validate')
    return parent

def test_task_post_validate_with_parent_and_default_collection(templar, mock_parent):
    # Set the default collection to trigger the branch
    AnsibleCollectionConfig.default_collection = "test.collection"

    # Create a Task instance with a mock parent
    task = Task()
    task._parent = mock_parent

    # Call post_validate to execute the missing lines
    task.post_validate(templar)

    # Assert that the parent's post_validate was called
    assert mock_parent.post_validate.called

    # Cleanup after the test
    AnsibleCollectionConfig.default_collection = None
