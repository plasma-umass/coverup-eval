# file lib/ansible/playbook/task_include.py:132-151
# lines [137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 149, 151]
# branches ['138->139', '138->149']

import pytest
from ansible.playbook.task_include import TaskInclude
from ansible.playbook.block import Block
from unittest.mock import MagicMock

# Mock classes to be used in the test
class MockPlay(object):
    pass

class MockRole(object):
    pass

class MockVariableManager(object):
    pass

class MockLoader(object):
    pass

@pytest.fixture
def task_include_fixture():
    # Setup the TaskInclude object with necessary mocks
    ti = TaskInclude()
    ti._parent = MagicMock(_play=MockPlay())
    ti._role = MockRole()
    ti._variable_manager = MockVariableManager()
    ti._loader = MockLoader()
    ti.args = {'apply': {'name': 'test_block'}}
    return ti

def test_build_parent_block_with_apply(task_include_fixture):
    # Test the build_parent_block method when 'apply' is provided
    p_block = task_include_fixture.build_parent_block()

    # Assertions to verify the postconditions
    assert isinstance(p_block, Block), "The returned object should be an instance of Block"
    assert p_block.block == [], "The block attribute should be an empty list"
    assert p_block.name == 'test_block', "The name attribute should be 'test_block'"

    # Cleanup: remove 'apply' from args to not affect other tests
    task_include_fixture.args.pop('apply', None)
