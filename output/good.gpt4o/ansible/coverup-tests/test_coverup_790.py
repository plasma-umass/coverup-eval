# file lib/ansible/playbook/block.py:389-390
# lines [389, 390]
# branches []

import pytest
from ansible.playbook.block import Block

class MockBase:
    pass

class MockConditional:
    pass

class MockCollectionSearch:
    pass

class MockTaggable:
    pass

@pytest.fixture
def block_instance():
    class TestBlock(Block, MockBase, MockConditional, MockCollectionSearch, MockTaggable):
        def __init__(self, block, rescue, always):
            self.block = block
            self.rescue = rescue
            self.always = always

    return TestBlock

def test_has_tasks_with_tasks(block_instance):
    block = block_instance(block=['task1'], rescue=[], always=[])
    assert block.has_tasks() is True

def test_has_tasks_with_rescue(block_instance):
    block = block_instance(block=[], rescue=['task1'], always=[])
    assert block.has_tasks() is True

def test_has_tasks_with_always(block_instance):
    block = block_instance(block=[], rescue=[], always=['task1'])
    assert block.has_tasks() is True

def test_has_tasks_with_no_tasks(block_instance):
    block = block_instance(block=[], rescue=[], always=[])
    assert block.has_tasks() is False
