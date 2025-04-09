# file lib/ansible/playbook/block.py:398-411
# lines [398, 405, 406, 407, 408, 409, 411]
# branches ['406->407', '406->411', '407->408', '407->409']

import pytest
from ansible.playbook.block import Block

# Mock class to simulate a parent that is not statically loaded
class MockParent:
    def __init__(self, statically_loaded):
        self.statically_loaded = statically_loaded

    def all_parents_static(self):
        return self.statically_loaded

@pytest.fixture
def setup_mock_parent(mocker):
    mocker.patch('ansible.playbook.task_include.TaskInclude', MockParent)

def test_all_parents_static_with_statically_loaded_parent(setup_mock_parent):
    block = Block()
    block._parent = MockParent(statically_loaded=True)
    assert block.all_parents_static() is True

def test_all_parents_static_with_non_statically_loaded_parent(setup_mock_parent):
    block = Block()
    block._parent = MockParent(statically_loaded=False)
    assert block.all_parents_static() is False

def test_all_parents_static_with_no_parent():
    block = Block()
    block._parent = None
    assert block.all_parents_static() is True
